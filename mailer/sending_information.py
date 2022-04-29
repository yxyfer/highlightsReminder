import os
from dotenv import load_dotenv


class SENDINGinformation(object):
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
