"""generate_highlights.py

description: Generates the final email (html + css) to be sent.

author: Mathieu Rivier
date: 04/29/2022
"""
from highlights_reminder import kindle_highlights, Quote


class GenerateHighlights(object):
    def __init__(self, file_path, quotes_number=5):
        """
        @arg file_path - the folder in which the quotes are
        """
        self.quotes_number = quotes_number
        self.quotes = kindle_highlights(file_path)

        self.highlights = self.generate_highlights()

    def generate_highlights(self):
        highlights = ""
        for quote in self.quotes.get_daily_n(self.quotes_number):
            highlights += self._format_quote(quote)

        return highlights

    def _format_quote(self, quote):
        formatted_quote = """
            <tr style='padding-top: 20px;'>
                <td align='center' class='container'>
        """

        formatted_quote += (
            """
                    <blockquote class='blockquote'>
                        <p class='quote'>
            """
            + quote.quote
            + """
                        </p>
                    </blockquote>
            """
        )

        formatted_quote += """
                    <div class ='quote_info'>
        """

        formatted_quote += "<H6 class='authors'>by: " + quote.authors + "</H6>"
        formatted_quote += "<H5 class ='title'>" + quote.title + "</H5>"

        formatted_quote += """
                    </div>
                </td>
            </tr>
        """

        return formatted_quote
