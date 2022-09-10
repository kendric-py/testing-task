from sqlalchemy.orm import Session

from core.utils import central_bank_rate, google_sheet, telegram
from core.database import queries, models
from core import config
import asyncio
import datetime
import time
import ast


class MainScraper:
    def __init__(self, session: Session):
        self.sheet = google_sheet.Sheet()
        self.bank = central_bank_rate.ParserXmlRatesBank()
        self.session = session

    def checker(self):
        """
        В данной функции выполняется проверка Google Таблицы, с помощью написанных классов мы получаем нужную информацию
        Получив данные с таблицы делаем проверки и записываем данные в БД.
        Переодичность проверки таблицы определается через конфиг файл, время указывается в секундах
        """
        while True:
            records = self.sheet.get_all_records()
            dollar_rate = ast.literal_eval(self.bank.get_currency_rate('R01235').get('value'))[0]
            sheet_orders_id, overdue_orders = [], []
            for record in records:
                try:
                    sheet_orders_id.append(int(record.get('заказ №')))
                    format_sheet_date = time.strptime(record.get('срок поставки'), '%d.%m.%Y')
                    date = time.strftime('%Y-%m-%d', format_sheet_date)
                    if time.strptime(date, '%Y-%m-%d') < time.strptime(str(datetime.datetime.now().date()), '%Y-%m-%d'):
                        overdue_orders.append(int(record.get('заказ №')))
                    queries.merge_order(self.session, int(record.get('заказ №')), 
                                        int(record.get('стоимость,$')), date, dollar_rate * int(record.get('стоимость,$')))
                except ValueError as error:
                    print(f'Error message: {error}')
                    continue
            if bool(len(overdue_orders)):
                asyncio.run(telegram.send_alert(', '.join(map(str, overdue_orders))))
                overdue_orders.clear()
            queries.delete_not_sheet_orders(self.session, sheet_orders_id)
            time.sleep(int(config.REFRESH_SHEET_SECONDS))

