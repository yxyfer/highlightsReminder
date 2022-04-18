import pandas as pd
import json
import random
import os
from io import StringIO


class Quote(object):
    def __init__(self, title, authors, quote) -> None:
        self.title = title
        self.authors = authors
        self.quote = quote

    def __repr__(self) -> str:
        return (
            "Quote(title: "
            + self.title
            + " authors: "
            + self.authors
            + " quote: "
            + self.quote
            + "); "
        )

    def __str__(self):
        return (
            "Quote(title: "
            + self.title
            + " authors: "
            + self.authors
            + " quote: "
            + self.quote
            + "); "
        )


class kindle_highlights(object):
    def __init__(self, books_dir) -> None:
        self.file_name = "quotesDirectory.csv"
        self.books_dir = books_dir
        self.books = self.get_book_file_names()
        self.quotes = self.load_highlights()

    def save_to_file(self, panda_data):
        print("hello " + str(panda_data))
        panda_data = panda_data.drop(
            columns="location", errors="ignore"
        ).drop_duplicates()
        panda_data.to_csv(self.file_name, index=False)

    def load_highlights(self):
        try:
            return pd.read_csv(self.file_name).drop_duplicates()
        except FileNotFoundError:
            return pd.DataFrame({"A": []})

    def get_book_file_names(self):
        with os.scandir(self.books_dir) as book_files:
            books = [self.books_dir + "/" + book.name for book in book_files]

        return books

    def load_new_books(self):
        new_data = self.load_new_highlights()
        panda_data = self.load_highlights()

        if not panda_data.empty:
            panda_data = pd.concat(
                [panda_data, new_data], ignore_index=True, sort=False, axis=0
            )
        else:
            panda_data = new_data

        self.save_to_file(panda_data)
        self.quotes = panda_data

    def load_new_books_from_text(self, title, authors, file_path):
        new_data = self.load_new_book_from_text(title, authors, file_path)
        panda_data = self.load_highlights()

        if not panda_data.empty:
            panda_data = pd.concat(
                [panda_data, new_data], ignore_index=True, sort=False, axis=0
            )
        else:
            panda_data = new_data

        self.save_to_file(panda_data)
        self.quotes = panda_data

    def load_new_book_from_text(self, title, authors, file_path):
        open_book = open(file_path, "r")
        quotes = []
        for quote in open_book:
            quotes.append(quote)

        data = {
            "text": quotes,
            "isNoteOnly": False,
            "note": None,
            "title": title,
            "authors": authors,
        }
        book = pd.DataFrame(data)

        open_book.close()

        return book

    def load_new_highlights(self):
        book_quotes = []
        for book in self.books:
            open_book = open(book)
            data = json.load(open_book)

            pd_data = pd.read_json(StringIO(json.dumps(data["highlights"])))
            pd_data["title"] = data["title"]
            pd_data["authors"] = data["authors"]

            open_book.close()
            book_quotes.append(pd_data)

        return pd.concat(book_quotes, ignore_index=True, sort=False)

    def get_daily_n(self, n):
        size = len(self.quotes)

        msg = []
        for _ in range(n):
            element = random.randint(0, size)
            quote = self.quotes.loc[element]

            msg.append(Quote(quote.title, quote.authors, quote.text))

        return msg
