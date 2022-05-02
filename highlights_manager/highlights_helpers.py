import os
import pandas as pd
from dotenv import load_dotenv


class HighlightsHelpers:
    def __init__(self):
        load_dotenv()

        self.ENV_QUOTES_FILE_NAME = self._get_quotes_csv_file_name()
        self.ENV_QUOTES_FOLDER_NAME = self._get_quotes_folder_name()

    def load(self):
        try:
            return pd.read_csv(self.ENV_QUOTES_FILE_NAME).drop_duplicates()
        except FileNotFoundError:
            return pd.DataFrame({"A": []})

    def save(self, panda_data):
        panda_data.drop_duplicates().to_csv(self.ENV_QUOTES_FILE_NAME, index=False)

    def _get_quotes_csv_file_name(self):
        ENV_QUOTES_FILE_NAME = os.getenv("QUOTES_CSV_FILE_NAME")

        return ENV_QUOTES_FILE_NAME

    def _get_quotes_folder_name(self):
        ENV_QUOTES_FOLDER_NAME = os.getenv("QUOTES_FOLDER_NAME")

        return ENV_QUOTES_FOLDER_NAME
