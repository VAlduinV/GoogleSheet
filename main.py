import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re


class GoogleSheet:
    def __init__(self, credentials_file, spreadsheet_id) -> None:
        self.credentials_file = credentials_file
        self.spreadsheet_id = spreadsheet_id
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials_file, self.scope
        )
        self.client = gspread.authorize(self.credentials)
        self.sheet = self.client.open_by_key(self.spreadsheet_id).sheet1

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def read_cell(self, cell):
        self.logger.info(f"Reading cell {cell}")
        return self.sheet.acell(cell).value

    def write_cell(self, cell, value):
        self.logger.info(f"Writing {value} to cell {cell}")
        self.sheet.update_acell(cell, value)

    def read_range(self, start_cell, end_cell):
        self.logger.info(f"Reading range {start_cell}:{end_cell}")
        return self.sheet.get(start_cell + ":" + end_cell)

    def write_range(self, start_cell, end_cell, values):
        self.logger.info(f"Writing range {start_cell}:{end_cell}")
        self.sheet.update(start_cell + ":" + end_cell, values)

    def append_row(self, values):
        self.logger.info(f"Appending row {values}")
        self.sheet.append_row(values)

    def find_telegram_channels(self, start_cell, end_cell):
        self.logger.info("Finding Telegram channels")
        values = self.sheet.get(start_cell + ":" + end_cell)
        telegram_channels = []
        pattern = r"https?://t\.me/[\w_]+"

        for row in values:
            for cell in row:
                matches = re.findall(pattern, cell)
                telegram_channels.extend(matches)

        return telegram_channels


if __name__ == "__main__":
    print(
        """
     ______   ______   ______   ______   __       ______   ______   __  __   ______   ______  ______  ______    
    /\  ___\ /\  __ \ /\  __ \ /\  ___\ /\ \     /\  ___\ /\  ___\ /\ \_\ \ /\  ___\ /\  ___\/\__  _\/\  ___\   
    \ \ \__ \\ \ \/\ \\ \ \/\ \\ \ \__ \\ \ \____\ \  __\ \ \___  \\ \  __ \\ \  __\ \ \  __\\/_/\ \/\ \___  \  
     \ \_____\\ \_____\\ \_____\\ \_____\\ \_____\\ \_____\\/\_____\\ \_\ \_\\ \_____\\ \_____\ \ \_\ \/\_____\ 
      \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_/\/_/ \/_____/ \/_____/  \/_/  \/_____/ 
                                                                                                                                                                                                           
        """
    )
    logging.basicConfig(level=logging.INFO)

    credentials_file = "service_account.json"
    spreadsheet_id = "1x76WBpDiAJj1XrLLoE3Lq6fZbGvC5marEeDScVnZB_0"
    google_sheet = GoogleSheet(credentials_file, spreadsheet_id)

    # Пример поиска телеграм-каналов в диапазоне значений
    telegram_channels = google_sheet.find_telegram_channels("G1", "G76")
    for count, row in enumerate(telegram_channels):
        print(f"Count: {count} -> {row}")

    # Пример чтения диапазона значений
    values = google_sheet.read_range("H1", "H76")
    for i, l in enumerate(values):
        for v in l:
            print(f"Index: {i} -> {v}")

