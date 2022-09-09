import gspread

from core import config


class Sheet:
    def __init__(self):
        google_account = gspread.service_account(filename=config.GOOGLE_CREDENTIALS_FILE_PATH)
        self.sheet = google_account.open(config.SHEET_NAME).sheet1

    def get_all_records(self) -> list[dict]:
        return(self.sheet.get_all_records())
