"""sending_information.py

description: Loads the sending information (receiver, sender)'s emails and
sender's password from the .env file. Makes those env variables available for
use in the program.

author: Mathieu Rivier
date: 04/29/2022
"""

import os
from dotenv import load_dotenv


class SendingInformation(object):
    def __init__(self):
        load_dotenv()

        self.ENV_RECIPIENT_EMAIL = self.get_recipient_email()

        self.ENV_SENDER_EMAIL = self.get_sender_email()
        self.ENV_SENDER_PASSWORD = self.get_sender_password()

    def get_recipient_email(self):
        ENV_RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

        return ENV_RECIPIENT_EMAIL

    def get_sender_email(self):
        ENV_SENDER_EMAIL = os.getenv("SENDER_EMAIL")

        return ENV_SENDER_EMAIL

    def get_sender_password(self):
        ENV_SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

        return ENV_SENDER_PASSWORD
