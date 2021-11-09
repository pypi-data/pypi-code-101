from django.core.mail import send_mail


class ConfirmationEmail:
    """
    A confirmation email message
    """

    subject = ""

    def __init__(self, email):
        self.email = email

    def get_subject(self):
        return self.subject

    def get_body(self, context: dict[str]) -> str:
        """
        Returns the body of the email message.
        :param context: contains at least the keys "pk" and "token"
        :return: a string with the body of the email message
        """
        return ""

    def send(self, context):
        send_mail(
            self.get_subject(),
            self.get_body(context),
            from_email=None,
            recipient_list=[self.email],
        )
