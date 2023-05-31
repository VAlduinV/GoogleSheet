import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
import sys


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
        self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def select_sheet(self, sheet_name: str):
        self.sheet = self.spreadsheet.worksheet(sheet_name.strip())

    def share(self, email: str, perm_type: str, role: str):
        self.spreadsheet.share(email, perm_type, role)
        self.logger.info(f"Shared with {email}")

    def read_cell(self, cell):
        self.logger.info(f"Reading cell {cell}")
        return self.sheet.acell(cell).value

    def write_cell(self, cell, value):
        self.logger.info(f"Writing {value} to cell {cell}")
        self.sheet.update_acell(cell, value)

    def read_range(self, start_cell: str, end_cell: str):
        self.logger.info(f"Reading range {start_cell}:{end_cell}")
        return self.sheet.get(start_cell + ":" + end_cell)

    def write_range(self, start_cell, end_cell, values):
        self.logger.info(f"Writing range {start_cell}:{end_cell}")
        self.sheet.update(start_cell + ":" + end_cell, values)

    def append_row(self, values):
        self.logger.info(f"Appending row {values}")
        self.sheet.append_row(values)

    def delete_rows(self, start, end):
        self.logger.info(f"Deleting rows {start} to {end}")
        self.sheet.delete_rows(start, end)

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


def write_to_file(filename: str, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")


def main(args):
    credentials_file = ""
    spreadsheet_id = ""

    google_sheet = GoogleSheet(credentials_file, spreadsheet_id)

    # Select a specific sheet
    google_sheet.select_sheet(args[0])

    # Share the spreadsheet with someone
    # google_sheet.share(args[1], 'user', 'writer')

    # Example of searching Telegram channels in a range of values
    telegram_channels = google_sheet.find_telegram_channels(args[1], args[2])
    google_sheet.logger.info(f"Found {len(telegram_channels)} Telegram channels.")

    for count, row in enumerate(telegram_channels):
        google_sheet.logger.info(f"Count: {count} -> {row}")

    write_to_file('telegram_channels.txt', telegram_channels)
    google_sheet.logger.info("Written Telegram channels to 'telegram_channels.txt'.")

    # Example of reading a range of values
    # values = google_sheet.read_range("H1", "H76")
    # for i, l in enumerate(values):
    #     for v in l:
    #         print(f"Index: {i} -> {v}")


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
    main(sys.argv[1:])
