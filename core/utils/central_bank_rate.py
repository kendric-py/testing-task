from lxml import etree
import requests
from core import config as cfg

class ParserXmlRatesBank:
    def __get_currency_rates(self) -> str | None:
        """Получение свежей информации по курсам валют от ЦБ России"""

        response = requests.get(url=cfg.CENTRAL_BANK_LINK)
        return(response.text)

    def __write_new_rates(self, rates_bank: str) -> str:
        """Запись в файл новых курсов валют"""

        with open(file=cfg.CACHE_RATES_BANK_PATH, mode='w') as xml_file:
            return(xml_file.write(rates_bank))

    def __find_target_currency(self, currency_id: str) -> dict:
        """Делаем поиск по ID валюты, и возвращаем полный результат."""
        tree: etree.ElementTree = etree.parse(cfg.CACHE_RATES_BANK_PATH)
        root = tree.getroot()
        all_currencies = root.findall('Valute')
        for currency in all_currencies:
            if currency.attrib.get('ID') != currency_id:
                continue
            return(
                {
                    'num_code': currency.find('NumCode').text,
                    'var_code': currency.find('CharCode').text,
                    'nominal': currency.find('Nominal').text,
                    'name': currency.find('Name').text,
                    'value': currency.find('Value').text,
                }
            )
                
    def get_currency_rate(self, currency_id: str) -> dict | None:
        """Основной метод запуска поиска валюты."""
        rates_bank = self.__get_currency_rates()
        self.__write_new_rates(rates_bank=rates_bank)
        return(self.__find_target_currency(currency_id))