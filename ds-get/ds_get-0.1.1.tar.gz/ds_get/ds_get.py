"""Main module."""
import argparse
import os
from typing import Iterable, Optional

import requests
from synology_api import downloadstation


CONFIG_ARGS = {
    "ip_address": {
        "nargs": "?",
        "type": str,
        "help": "Synology DS IP (or use DSGET_IP_ADDRESS env var)",
    },
    "port": {
        "nargs": "?",
        "type": int,
        "help": "Synology DS port (or use DSGET_PORT env var)",
    },
    "username": {
        "nargs": "?",
        "type": str,
        "help": "Synology DS username (or use DSGET_USERNAME env var)",
    },
    "password": {
        "nargs": "?",
        "type": str,
        "help": "Synology DS Password (or use DSGET_PASSWORD env var)",
    },
    "secure": {"nargs": "?", "type": bool, "help": "HTTPS?", "default": True},
    "cert_verify": {"nargs": "?", "type": bool, "default": False},
    "dsm_version": {
        "nargs": "?",
        "type": str,
        "help": "Synology DS Version",
        "default": "7",
    },
    "debug": {"nargs": "?", "type": bool, "default": False},
}


class DSGetClientException(Exception):
    pass


class DSGetClient(object):
    def __init__(
        self,
        ip_address: str,
        port: int,
        username: str,
        password: str,
        secure=True,
        cert_verify=True,
        dsm_version=7,
        debug=False,
    ):
        if not all([ip_address, port, username, password]):
            raise DSGetClientException("You must at least set the ip address, port, username and password")
        try:
            self.client = downloadstation.DownloadStation(
                ip_address,
                port,
                username,
                password,
                secure=secure,
                cert_verify=cert_verify,
                dsm_version=dsm_version,
                debug=debug,
            )
        except requests.exceptions.RequestException as e:
            raise DSGetClientException(e)

    def add_links(self, links: Iterable[str]) -> tuple:
        """Add a list of links to be downloaded

        Args:
            links (Iterable[str]): Magnet, torrent or file links

        Returns:
            tuple: A list of additions and errors
        """

        adds = errors = []
        for link in links:
            task = self.client.create_task(link)
            if task and task.get("success", False):
                adds.append(task)
            else:
                errors.append((link, task))
        return adds, errors

    def tasks(self, task_id=Optional[int]):
        return self.client.tasks_list().get("data", {}).get("tasks", [])


def parse_arguments() -> argparse.Namespace:
    description = (
        "Thin client for interfacing with Synology DownloadStation.\n"
        "Primarily used to add magnet and torrent files.\n"
        "Associate magnet: and .torrent uris with this script in your browser and "
        "directly start them in your Synology DS"
    )
    parser = argparse.ArgumentParser(
        "ds_get",
        description=description,
        epilog="""
    The arguments can also be set in env:
        DSGET_IP_ADDRESS
        DSGET_PORT
        DSGET_USERNAME
        DSGET_PASSWORD
        DSGET_SECURE
        DSGET_CERT_VERIFY
        DSGET_DSM_VERSION
        DSGET_DEBUG
    """,
    )

    for key, config_kwgs in CONFIG_ARGS.items():
        parser.add_argument(f"--{key}", **config_kwgs)

    parser.add_argument("links", nargs="+", help="Magnet Links or file URIs")
    args = parser.parse_args()

    return args


def load_config_from_env_args(args: argparse.Namespace) -> dict:
    config = {}
    for key, config_kwgs in CONFIG_ARGS.items():
        environ_key = f"DSGET_{key.upper()}"
        config[key] = os.environ.get(environ_key, None)
        if config[key] is None or (config[key] is not None and config_kwgs.get("default", False)):
            config[key] = getattr(args, key)
    return config
