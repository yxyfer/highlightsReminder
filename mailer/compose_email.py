"""compose_email.py

description: Generates the email to be sent to recipient. And returns it
through the variable message.

author: Mathieu Rivier
date: 04/29/2022
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class ComposeEmail(object):
    def __init__(self, sending_info, highlights):
        self.sending_info = sending_info
        self.highlights = highlights

        self.message = self.get_mail_header()

        self.css = self.get_mail_css()
        self.body = self.get_mail_body()

        self.get_mail()

    def get_mail(self):
        plain = MIMEText("", "plain")
        html = MIMEText(self.css + self.body, "html")

        self.message.attach(plain)
        self.message.attach(html)

    def get_mail_header(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "Daily 5 - Book Quotes"
        message["From"] = self.sending_info.ENV_SENDER_EMAIL
        message["To"] = self.sending_info.ENV_RECIPIENT_EMAIL

        return message

    def get_mail_body(self):
        mail_body = """
        <html>
          <body>
            <h1> Matt's Daily Quotes </h1>

            <table
                width='100%'
                align='center'
                border='0'
                cellspacing='0'
                cellpadding='0'
            >
                <tr>
                    <td align="center">
                        <table
                            width="600"
                            border="0"
                            cellspacing="0"
                            cellpadding="0"
                        >
        """

        mail_body += self.highlights

        mail_body += """
                        </table>
                    </td>
                </tr>
            </table>
          </body>
        </html>
        """

        return mail_body

    def get_mail_css(self):
        css = """\
        <style>
        @media screen and (max-width: 530px) {
            .blockquote p {
                font-family: 'Times New Roman';
                font-size: 26px;
                font-weight: bold;
            }

            .blockquote:before {
                position: absolute;
                font-family: 'Times New Roman';
                top: 0;
                line-height: .655;
                left: -10px;
                content: '“';
                font-size: 250px;
                color: rgba(0,0,0,0.1);
            }
        }
        @media screen and (min-width: 531px) {
            .blockquote p {
                font-family: 'Times New Roman';
                font-size: 26px;
                font-weight: bold;
            }

            .blockquote:before {
                position: absolute;
                font-family:  'Times New Roman';
                top: 0;
                line-height: .655;
                left: -50px;
                content: '“';
                font-size: 250px;
                color: rgba(0,0,0,0.1);
            }
        }
        table {
            border-spacing: 0px 30px;
        }
        .blockquote {
            position: relative;
        }

        .container {
            border-radius: 25px;
            border: 2px solid #73AD21;
            padding: 20px;
            height: auto;
        }
        .quote_info {
            text-align: right;
        }
        H5.title {
            text-decoration: underline;
            margin-top: 0;
            margin-bottom: 0;
            line-height: 1;
            font-size: 15px;
        }
        H6.authors {
            color: grey;
            margin: 0;
            padding: 0;
            font-size: 13px;
        }
        .quote {
            text-align: justify;
            font-size: 21px;
        }
        </style>
        """

        return css
