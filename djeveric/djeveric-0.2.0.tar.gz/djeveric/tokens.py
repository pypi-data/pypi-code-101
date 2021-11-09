from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ConfirmationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, instance, timestamp):
        data = instance.get_confirmation_token_data()
        data = "".join([str(item) for item in data])
        return f"{data}{timestamp}"
