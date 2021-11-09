from djeveric.fields import ConfirmationField
from djeveric.tokens import ConfirmationTokenGenerator


class ConfirmableModelMixin:
    """
    Mixin for models which can be confirmed via email.
    """

    token_generator = ConfirmationTokenGenerator()

    def confirm(self) -> None:
        """
        Confirms the model instance.
        """
        setattr(self, self._get_confirmation_field().name, True)
        self.save()

    def get_confirmation_email_recipient(self) -> str:
        """
        Returns the email address where to send the confirmation email.

        :return: a string containing an email address
        """
        assert hasattr(self, "email"), "Implement get_confirmation_email_recipient()"
        return self.email

    def check_confirmation_token(self, token):
        return self.token_generator.check_token(self, token)

    def get_confirmation_token(self):
        return self.token_generator.make_token(self)

    def get_confirmation_token_data(self) -> list:
        """
        Returns the data on which confirmation token generation is based. The data is converted to strings and hashed
        with a salt.

        The data should
        - differentiate the model instance (e.g. by using the pk) and
        - change on confirmation of the model instance.

        :return: a list of data items
        """
        return [self.pk, self.get_confirmation_email_recipient(), self._is_confirmed()]

    def save(self, **kwargs):
        super().save(**kwargs)
        if not self._is_confirmed() and self._has_confirmation_recipient():
            self._send_request()

    def _get_confirmation_field(self):
        for field in self._meta.get_fields(False, False):
            if isinstance(field, ConfirmationField):
                return field
        assert False, "You must specify a ConfirmationField on a confirmable model"

    def _get_confirmation_email(self):
        return self._get_confirmation_field().confirmation_email_class(
            self.get_confirmation_email_recipient()
        )

    def _has_confirmation_recipient(self):
        """Returns True if a confirmation request can be sent."""
        return True

    def _is_confirmed(self):
        return getattr(self, self._get_confirmation_field().name)

    def _send_request(self):
        assert not self._is_confirmed()
        self._get_confirmation_email().send(
            {
                "pk": self.pk,
                "token": self.token_generator.make_token(self),
            }
        )
