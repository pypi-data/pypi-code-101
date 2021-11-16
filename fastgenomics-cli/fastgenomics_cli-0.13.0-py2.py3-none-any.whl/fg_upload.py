import argparse
import logging
import sys
from getpass import getpass
from glob import glob

from fastgenomics import FASTGenomicsClient, FASTGenomicsDatasetClient
from update_checker import update_check

from . import __version__
from .fg_cli import (
    format_type_list,
    get_dataset_types,
    output,
    prompt_dataset_type,
)

log = logging.getLogger(__name__)

PLATFORM = "https://beta.fastgenomics.org/"


def main():
    print(f"FASTGenomics upload tool version {__version__}")
    update_check("fastgenomics_upload", __version__)

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "file", nargs="+", type=str, help="the file(s) to be uploaded"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="more verbose output"
    )
    parser.add_argument(
        "-d",
        "--dataset",
        help="add file to existing dataset with this id",
        type=str,
        default=None,
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
        "-t",
        "--title",
        type=str,
        default=None,
        help="the title of the new dataset",
    )
    parser.add_argument(
        "-m",
        "--metadata",
        help="upload files as metadata instead of expression data",
        action="store_true",
    )
    parser.add_argument(
        "--dataset_type", help="the dataset type", type=str, default=None
    )
    parser.add_argument(
        "--url", help="The platform url", type=str, default=PLATFORM
    )
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        format="%(asctime)s [%(name)-19.19s] [%(levelname)-3.3s] %(message)s"
        # level=log_level
    )
    log.setLevel(log_level)
    FASTGenomicsClient.set_log_level(log_level)

    if args.dataset is not None and args.title is not None:
        log.error(
            "When adding files to an existing dataset, you can't specify the dataset's title"
        )
        sys.exit(1)

    client = FASTGenomicsDatasetClient()

    if (
        args.user is not None
        or args.password is not None
        or not client.is_logged_in()
    ):
        if args.user is None:
            args.user = input("Please enter your username: ")
        if args.password is None:
            args.password = getpass("Please enter your password: ")
        try:
            client.login(
                args.user, args.password, login_method="password", url=args.url
            )
        except:
            log.error(
                "Login failed. Did you provide the correct username and password?"
            )
            sys.exit(1)

    if args.dataset is None:
        if args.dataset_type is None:
            args.dataset_type = prompt_dataset_type()
        if args.title is None:
            args.title = input(
                f"Please enter the title of the dataset you want to create: [default: {args.file[0]}] "
            )
        if args.title is None or args.title == "":
            args.title = args.file[0]
        log.info(f"creating dataset with title '{args.title}'")
        try:
            r = client.create_dataset(args.title, args.dataset_type)
            args.dataset = r.json()["id"]
        except Exception as e:
            log.error(f"Failed to create dataset: {e}")
            sys.exit(1)

    results = []
    for file_arg in args.file:
        filelist = glob(file_arg)
        for file in filelist:
            log.info(f"uploading '{file}'")
            try:
                result = client.add_file_to_dataset(
                    args.dataset,
                    file,
                    "metadata" if args.metadata else "expressiondata",
                    show_progress_bar=True,
                )
                results.append(result)

            except Exception as e:
                log.error(f"Failed to upload '{file}': {e}")
                exit(1)
    log.info("SUCCESS! Files(s) uploaded:\n")
    output(results)

    print('\n\nLogout using "fg-cli logout" when you are done.')


if __name__ == "__main__":
    main()
