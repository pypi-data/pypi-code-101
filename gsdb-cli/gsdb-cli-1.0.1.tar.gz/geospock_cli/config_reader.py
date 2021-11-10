# Copyright (c) 2014-2021 GeoSpock Ltd.

import json
from pathlib import Path

from .keyring import Keyring

from .constants import messages
from .exceptions import CLIError

GEOSPOCK_DIR = Path.home().joinpath(".geospock")
CONFIG_FILE = GEOSPOCK_DIR.joinpath("config.json")


class ConfigReaderAndWriter:
    def __init__(self, profile: str):
        self.profile = profile
        self.keyring = Keyring(profile)

    def write_login(self, username: str,
                    password: str,
                    request_address: str,
                    ca_cert_file,
                    disable_verification: bool):
        if username is None or password is None or request_address is None:
            raise CLIError(messages.helpLogin)
        Path(GEOSPOCK_DIR).mkdir(parents=True, exist_ok=True)
        current_config = self.get_config()
        try:
            current_config[self.profile] = dict(request_address=request_address,
                                                ca_cert_file=ca_cert_file,
                                                disable_verification=disable_verification)
        except Exception:
            raise CLIError("Could not generate configuration entry from provided request address.")
        config_path = Path(CONFIG_FILE)
        with config_path.open(mode="w") as config_file_write:
            config_file_write.write(json.dumps(current_config, indent=4))
        self.keyring.set_credentials(username, password)

    def write_logout(self):
        config = self.get_config()
        if self.profile != "default" and self.profile not in config:
            raise CLIError(f"The profile '{self.profile}' does not exist.")
        config.pop(self.profile, None)
        config_path = Path(CONFIG_FILE)
        Path(GEOSPOCK_DIR).mkdir(parents=True, exist_ok=True)
        with config_path.open(mode="w") as config_file_write:
            config_file_write.write(json.dumps(config, indent=4))
        self.keyring.delete_credentials()

    def decode(self):
        user, password = self.keyring.get_credentials_with_retry()
        if user is None or password is None:
            raise CLIError(messages.insufficientLoginDetails)
        return user, password

    def get_config(self) -> dict:
        config_path = Path(CONFIG_FILE)
        if config_path.exists() and config_path.stat().st_size > 0:
            with config_path.open() as json_file:
                try:
                    config_all = json.load(json_file)
                except json.JSONDecodeError:
                    raise CLIError(messages.invalidConfig)
            return config_all
        else:
            return {}
