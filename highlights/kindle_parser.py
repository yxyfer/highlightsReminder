from io import StringIO
import pandas as pd
import json
import os

from highlights.helpers import HighlightsHelpers


class HighlightsParserKindle:
    def __init__(self):
        self.hhelpers = HighlightsHelpers()

        self.highlights_files = self._get_highlights_files()
        self.new_highlights = self._parse_new_highlights()
        self.highlights = self._merge_new_highlights()

        self._clean_and_save()

    def _get_highlights_files(self):
        folder_name = self.hhelpers.ENV_QUOTES_FOLDER_NAME
        suffix = ".json"

        highlights_files = [
            highlights_file.path
            for highlights_file in os.scandir(folder_name)
            if highlights_file.name.endswith(suffix)
        ]

        return highlights_files

    def _parse_new_highlights(self):
        new_highlights = []

        for file in self.highlights_files:
            highlight_file = open(file, "r")
            data = json.load(highlight_file)

            pd_data = pd.read_json(StringIO(json.dumps(data["highlights"])))
            pd_data["title"] = data["title"]
            pd_data["authors"] = data["authors"]

            highlight_file.close()
            new_highlights.append(pd_data)

        return pd.concat(new_highlights, ignore_index=True, sort=False)

    def _merge_new_highlights(self):
        existing_highlights = self.hhelpers.load()

        if not existing_highlights.empty:
            highlights = pd.concat(
                [existing_highlights, self.new_highlights],
                ignore_index=True,
                sort=False,
                axis=0,
            )
        else:
            highlights = self.new_highlights

        return highlights

    def _clean_and_save(self):
        self.highlights = self.highlights.drop(columns="location", errors="ignore")
        self.hhelpers.save(self.highlights)
