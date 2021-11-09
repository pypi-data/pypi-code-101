import argparse

from .info import clear_info_cache
from .actions import auth


def main():
    parser = argparse.ArgumentParser(
        description='Tools for YKPS.'
    )

    avail = {
        'clear_cache': clear_info_cache,
        'auth': auth
    }

    parser.add_argument('action', choices=avail, help='the action to perform')
    args = parser.parse_args()

    action = args.action

    avail[action]()
