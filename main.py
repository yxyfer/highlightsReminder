"""main.py

description: This file aggregates all the others from this program :)

author: Mathieu Rivier
date:   04/29/2022
"""

from mailer.sending_information import SendingInformation
from mailer.generate_highlights import GenerateHighlights
from mailer.compose_email import ComposeEmail
from mailer.send_mail import send_mail


if __name__ == "__main__":
    sending_info = SendingInformation()

    highlights = GenerateHighlights("books").highlights

    mail = ComposeEmail(sending_info, highlights).message

    send_mail(sending_info, mail)
