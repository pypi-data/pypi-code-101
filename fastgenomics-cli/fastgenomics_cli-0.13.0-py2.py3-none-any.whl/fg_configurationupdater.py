__version__ = "1.0.0"

from fastgenomics import FASTGenomicsPlatformUpdater, FASTGenomicsClient
import argparse
import logging
import sys
from getpass import getpass

logger = logging.getLogger(__name__)

PLATFORM = "https://beta.fastgenomics.org/"


def main():
    print(f"FASTGenomics updater tool version {__version__}")

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "directories", nargs="+", type=str, help="the directories to be uploaded"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="more verbose output"
    )

    parser.add_argument(
        "-u",
        "--user",
        type=str,
        default=None,
        help="your username (or email address)",
    )
    parser.add_argument(
        "-p", "--password", type=str, default=None, help="your password"
    )

    parser.add_argument(
        "--url", help="The platform url", type=str, default=PLATFORM
    )
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    log_format = "[%(asctime)s] - %(message)s"
    logging.basicConfig(
        format=log_format,
        level=log_level
    )

    updater = FASTGenomicsPlatformUpdater("")
    if (
        args.user is not None
        or args.password is not None
        or not updater.is_logged_in()
    ):
        if args.user is None:
            args.user = input("Please enter your username: ")
        if args.password is None:
            args.password = getpass("Please enter your password: ")
        try:
            updater.login(
                args.user, args.password, login_method="password", url=args.url
            )
        except:
            logger.error(
                "Login failed. Did you provide the correct username and password?"
            )
            sys.exit(1)

    if not updater.is_logged_in():
        updater.login()

    for directory in args.directories:
        updater = FASTGenomicsPlatformUpdater(directory)
        updater.update()


if __name__ == "__main__":
    main()
