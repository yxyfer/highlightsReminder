"""send_mail.py

description: sends the final email generated before and passed in as argument.

author: Mathieu Rivier
date: 04/29/2022
"""

import smtplib
import ssl


def send_mail(sending_info, message):
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sending_info.ENV_SENDER_EMAIL, sending_info.ENV_SENDER_PASSWORD)
        server.sendmail(
            sending_info.ENV_SENDER_EMAIL,
            sending_info.ENV_RECIPIENT_EMAIL,
            message.as_string(),
        )
