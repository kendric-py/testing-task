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
        while True:
            records = self.sheet.get_all_records()
            dollar_rate = self.bank.get_currency_rate('R01235').get('value')
            overdue_orders = []
            for record in records:
                format_sheet_date = time.strptime(record.get('срок поставки'), '%d.%m.%Y')
                date = time.strftime('%Y-%m-%d', format_sheet_date)
                if time.strptime(date, '%Y-%m-%d') < time.strptime(str(datetime.datetime.now().date()), '%Y-%m-%d'):
                    overdue_orders.append(record.get('заказ №'))
                    continue
                try:
                    queries.merge_order(
                        self.session, 
                        int(record.get('заказ №')), 
                        int(record.get('стоимость,$')), 
                        date,
                        ast.literal_eval(dollar_rate)[0] * int(record.get('стоимость,$'))
                    )
                except ValueError as error:
                    print(f'Error message: {error}')
                    continue
            if bool(len(overdue_orders)):
                asyncio.run(telegram.send_alert(overdue_orders))
                overdue_orders.clear()

            queries.delete_overdue_orders(self.session)
            print('del')
            time.sleep(int(config.REFRESH_SHEET_SECONDS))

