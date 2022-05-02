"""quote.py

description:

author: Mathieu Rivier
date: 04/29/2022
"""


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
