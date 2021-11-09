from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ConfirmationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, instance, timestamp):
        data = list(instance.get_confirmation_token_data())
        assert all(
            isinstance(item, str) for item in data
        ), f"Iterable returned by {instance.__class__.__name__}.get_confirmation_token_data must contain strings."
        serialized_data = "".join(data)
        return f"{serialized_data}{timestamp}"
