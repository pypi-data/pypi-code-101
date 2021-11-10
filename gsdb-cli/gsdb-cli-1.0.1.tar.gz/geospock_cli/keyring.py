# Copyright (c) 2014-2021 GeoSpock Ltd.

import os
import keyring
from keyrings.cryptfile.cryptfile import CryptFileKeyring
from getpass import getpass
from .exceptions import CLIError
from .constants import envvars
import click
from keyring.errors import NoKeyringError
from tenacity import retry, wait_fixed, stop_after_attempt
from .constants import messages


class KeyringNotConfigured(RuntimeError):
    pass


class Keyring:
    def __init__(self, profile: str):
        self.profile = profile
        self.keyring = None

    def init_keyring(self, prompt_if_creation_required=False):
        if self.keyring is None:
            self.keyring = Keyring.get_key_ring(prompt_if_creation_required)

    def set_credentials(self, username, password):
        try:
            self.init_keyring(True)
            self.keyring.set_password("geospock", self.profile + "-username", username)
            self.keyring.set_password("geospock", self.profile + "-password", password)
        except (NoKeyringError, KeyringNotConfigured):
            raise CLIError(messages.keyringRequired)

    def delete_credentials(self):
        try:
            self.init_keyring()
            self.keyring.delete_password("geospock", self.profile + "-username")
            self.keyring.delete_password("geospock", self.profile + "-password")
        except (keyring.errors.PasswordDeleteError, KeyringNotConfigured):
            pass

    @retry(reraise=True, stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _get_credentials(self):
        self.init_keyring()
        user = self.keyring.get_password("geospock", self.profile + "-username")
        password = self.keyring.get_password("geospock", self.profile + "-password")
        return user, password

    def get_credentials_with_retry(self):
        try:
            self.init_keyring()
            return self._get_credentials()
        except (NoKeyringError, KeyringNotConfigured):
            raise CLIError(messages.insufficientLoginDetails)
        except keyring.errors.KeyringError:
            raise CLIError("Cannot retrieve login details from Keyring")

    @staticmethod
    def get_key_ring(prompt_if_creation_required):
        kr = Keyring.get_highest_priority_keyring_backend(keyring.get_keyring())
        if type(kr) is CryptFileKeyring:
            if not os.path.isfile(kr.file_path):
                prompt = ("Unable to find a keyring to securely store your password. \n"
                          "Do you want to create an encrypted keyring backend in your HOME directory?")
                if not (prompt_if_creation_required and click.confirm(prompt, default=True, prompt_suffix=': ',
                                                                      show_default=True, err=True)):
                    raise KeyringNotConfigured()

            try:
                kr.keyring_key = os.getenv(envvars.keyring_password) \
                                 or getpass("Please enter the master password for encrypted keyring: ")
            except ValueError:
                raise CLIError("Incorrect keyring password provided.")

        return kr

    @staticmethod
    def get_highest_priority_keyring_backend(kr):
        if type(kr) is keyring.backends.chainer.ChainerBackend:
            return kr.backends[0]
        return kr
