import random

from highlights_manager.quote import Quote
from highlights_manager.highlights_helpers import HighlightsHelpers


class HighlightsInteractions(object):
    def __init__(self):
        self.quotes = HighlightsHelpers().load()

    def get_daily_n(self, n):
        size = len(self.quotes)

        daily_quotes = []
        for _ in range(n):
            element = random.randint(0, size)
            quote = self.quotes.loc[element]
            # try quote = Quote(self.quotes.loc[element])
            daily_quotes.append(Quote(quote.title, quote.authors, quote.text))

        return daily_quotes
