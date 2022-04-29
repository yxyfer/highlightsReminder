class Sending_information_v1(object):
    def __init__():
        """
        These can be manually hard coded.
        It can make it less daunting than to have to rewrite the sender and
        recipient email addresses every time.
        """
        recipient_email = get_recipient_email()
        sender_email = get_sender_email()
        sender_password = get_sender_password()

    def get_recipient_email():
        recipient_email = input("Type your receiver's email and press enter:")

        return recipient_email

    def get_sender_email():
        sender_email = input("Type sender's email and press enter:")

        return sender_email

    def get_sender_password():
        password = input(
            "Type your password for senders email and press enter:"
            + "(note this is not super secure - use a test email)"
        )

        return password
