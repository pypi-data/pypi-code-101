#!/usr/bin/env python3

"""
FASTGenomics Commandline Interface (CLI)
"""

__copyright__ = "Copyright, Comma Soft AG"
__maintainer__ = "Ralf Karle"
__email__ = "ralf.karle@comma-soft.com"

import argparse
import datetime
import json
import logging
import sys
from getpass import getpass
from os import path

from fastgenomics import (
    FASTGenomicsClient,
    FASTGenomicsDatasetClient,
    FASTGenomicsLargeFileStorageClient,
    ToolConfiguration,
)
from fastgenomics import __version__ as fg_version
from fastgenomics import run_zip

from . import __version__

VERSIONS = {
    "FASTGenomics CLI version": __version__,
    "FASTGenomics client version": fg_version,
}

logger = logging.getLogger(__name__)
log_level = logging.WARN


def output(data: dict):
    """ output """
    j = json.dumps(data, indent=4)
    print(j)


def _add_parser(
    parser,
    name: str,
    helptext: str,
    description: str = "",
    epilog: str = "",
    action: str = "",
):
    if description == "":
        description = helptext

    if action == "":
        action = name

    if epilog == "":
        new_parser = parser.add_parser(
            name, help=helptext, description=description
        )
    else:
        new_parser = parser.add_parser(
            name,
            help=helptext,
            description=description,
            epilog=epilog,
            formatter_class=argparse.RawTextHelpFormatter,
        )

    new_parser.set_defaults(action=action)

    new_parser.add_argument(
        "-v",
        "--verbose",
        help="Activate verbose output",
        action="count",
        default=0,
    )

    return new_parser


def parse_args():
    desc = fR"""
 ______       _____ _______ _____                            _
|  ____/\    / ____|__   __/ ____|                          (_)
| |__ /  \  | (___    | | | |  __  ___ _ __   ___  _ __ ___  _  ___ ___
|  __/ /\ \  \___ \   | | | | |_ |/ _ \ '_ \ / _ \| '_ ` _ \| |/ __/ __|
| | / ____ \ ____) |  | | | |__| |  __/ | | | (_) | | | | | | | (__\__ \
|_|/_/    \_\_____/   |_|  \_____|\___|_| |_|\___/|_| |_| |_|_|\___|___/

Welcome to FASTGenomics CLI!
Version {__version__}

Here are the base commands:
"""
    parser = argparse.ArgumentParser(
        description=desc, formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(
        title="FASTGenomics CLI",
        help="Actions for FASTGenomics",
    )

    login_parser = _add_parser(
        subparsers, "login", helptext="Log in to the platform."
    )
    login_parser.add_argument("-u", "--user", help="the platform user")
    login_parser.add_argument(
        "-p",
        "--passphrase",
        help="the passphrase of platform user. You might need to wrap it in single quotes (').",
    )
    login_parser.add_argument(
        "-m",
        "--login_method",
        help="the login method 'pat' (personal access token), 'password' or 'bearer'. Default: pat",
        choices=["pat", "password", "bearer"],
        default="pat",
    )

    login_parser.add_argument(
        "--url",
        help="the url of the plattform. For Example: https://beta.fastgenomics.org",
    )

    logout_parser = _add_parser(
        subparsers,
        "logout",
        helptext="Log out to remove access to the platform.",
    )

    aws_parser = _add_parser(
        subparsers, "configure-aws", helptext="Configure AWS for the platform"
    )

    epilog = f"""
output:

{json.dumps(VERSIONS, indent=4)}
"""
    version_parser = _add_parser(
        subparsers,
        "version",
        helptext="Show the version of FASTGenomics CLI.",
        description="Show the version of the cli client",
        epilog=epilog,
    )

    lfs_parser = _add_parser(
        subparsers,
        "lfs",
        helptext="Manage Large File Storage (lfs)",
        description="Group: fg lfs  - Manage platform Large File Storage (lfs)",
    )

    lfs_subparsers = lfs_parser.add_subparsers()

    lfs_create_parser = _add_parser(
        lfs_subparsers,
        "create",
        action="lfs-create",
        helptext="Create and upload a large file storage",
    )

    lfs_create_parser.add_argument(
        "files_or_directory",
        nargs="+",
        type=str,
        help="file names or directory to be compressed",
    )

    lfs_create_parser.add_argument(
        "-z", "--zip-filename", help="name of the zip file", type=str, nargs="?"
    )

    lfs_create_parser.add_argument(
        "-P",
        "--zip-password",
        help="password for the zip file. if omitted a password will be generated.",
        type=str,
        nargs="?",
        required=False,
    )

    lfs_create_parser.add_argument(
        "-r",
        "--recipient-email",
        help="the email address used in the platform of the recipient",
        type=str,
        required=True,
    )

    lfs_create_parser.add_argument(
        "-T",
        "--title",
        help="the title of the  dataset containing the uploaded data",
        type=str,
        nargs="?",
        default="",
    )

    lfs_create_parser.add_argument(
        "--provider",
        help="the provider to be used 'azure' or 'aws'. Default: azure)",
        type=str,
        default="azure",
        nargs="?",
        choices=["azure", "aws"],
    )

    lfs_create_parser.add_argument(
        "--skip-compression", help="Skip the compression", action="store_true"
    )

    lfs_get_url_parser = _add_parser(
        lfs_subparsers,
        "get-url",
        helptext="Get a download url",
        action="lfs-get-downloadurl",
    )
    lfs_get_url_parser.add_argument(
        "id", type=str, help="the id of the storage"
    )
    lfs_get_url_parser.add_argument(
        "access_token", type=str, help="the access token"
    )

    # ###### datasets #####

    dataset_parser = subparsers.add_parser(
        "dataset",
        help="Manage datasets",
        description="Group: fg dataset  - Manage datasets.",
    )

    dataset_subparsers = dataset_parser.add_subparsers()

    dataset_types_parser = _add_parser(
        dataset_subparsers,
        "get-types",
        action="get-types",
        helptext="get available dataset types together with their name and description",
    )

    dataset_detail_parser = _add_parser(
        dataset_subparsers,
        "get-type-details",
        action="get-type-details",
        helptext="shows all editable fields for a dataset type",
    )

    dataset_detail_parser.add_argument(
        "-m",
        "--mode",
        help='description mode. Either "full" or "brief". Default "brief".',
        type=str,
        choices=["brief", "full"],
        default="brief",
    )
    dataset_detail_parser.add_argument(
        "id",
        help="the id of the dataset type",
        type=str,
        nargs="?",
        default=None,
    )

    dataset_create_parser = _add_parser(
        dataset_subparsers,
        "create",
        action="dataset-create",
        helptext="create a dataset",
    )

    dataset_create_parser.add_argument(
        "-T",
        "--title",
        help="the title of the dataset",
        type=str,
    )

    dataset_create_parser.add_argument(
        "--dataset_type",
        help='the dataset type. For example "cs-singlecell". To get an overview of available types use `fg-cli dataset get-types`',
        type=str,
    )

    dataset_upload_parser = _add_parser(
        dataset_subparsers,
        "upload-file",
        action="dataset-upload",
        helptext="upload files to dataset",
    )
    dataset_upload_parser.add_argument(
        "files",
        nargs="+",
        type=str,
        help="file names of the files to be uploaded",
    )
    dataset_upload_parser.add_argument(
        "-id", help="the id of the dataset", type=str
    )

    dataset_upload_parser.add_argument(
        "-t",
        "--type",
        help="the type of the file 'primaryData' or 'metaData': Default: primaryData",
        type=str,
        default="primarydata",
        nargs="?",
        choices=["primarydata", "metadata"],
    )

    dataset_set_metadata_parser = _add_parser(
        dataset_subparsers,
        "set-metadata",
        action="dataset-set-metadata",
        helptext="set the metadata for a dataset",
    )

    dataset_set_metadata_parser.add_argument(
        "-id", help="the id of the dataset", type=str
    )

    dataset_set_metadata_parser.add_argument(
        "metadata",
        help="the metadate to set. Use @<filename> to provide the data by file or '{ json }'. Depending on your system you might have to escape quotes accordingly.",
        type=str,
    )

    dataset_delete_parser = _add_parser(
        dataset_subparsers,
        "delete",
        action="dataset-delete",
        helptext="delete a dataset",
    )
    dataset_delete_parser.add_argument(
        "id", help="the id of the dataset", type=str
    )

    args = parser.parse_args()
    return parser, args


def get_dset_details(id: str, mode="brief") -> dict:
    client = FASTGenomicsDatasetClient()
    editable_fields = client.get_dataset_editable_fields(id).json()
    dataset_details = client.get_dataset_type_by_id(id).json()
    main_fields = ["id", "name", "description", "version", "vendor"]

    output = {}
    for f in main_fields:
        output[f] = dataset_details[f]
    output["editable_fields"] = editable_fields

    if mode == "brief":
        return output
    elif mode == "full":
        output["extended_properties"] = dataset_details["properties"]
        return output
    else:
        raise KeyError(f'"mode" must be "brief" or "full" not {mode}')


def get_dataset_types(numbered: bool = False):
    client = FASTGenomicsDatasetClient()
    result = client.get_dataset_types()
    if numbered:
        types = {
            n: {
                "id": type["id"],
                "name": type["name"],
                "description": type["description"],
            }
            for n, type in enumerate(result.json()["list"])
        }
    else:
        types = {
            type["id"]: {
                "name": type["name"],
                "description": type["description"],
            }
            for type in result.json()["list"]
        }
    return types


def format_type_list(type_list: dict):
    pretty = "\n" + "=" * 23 + "\nAvailable dataset types\n" + "=" * 23 + "\n\n"

    for type in type_list:
        pretty += (
            f"[{type}]".ljust(6, " ")
            + (" " * 6).join(
                [
                    f"{i[0]}:".ljust(15, " ") + i[1] + "\n"
                    for i in type_list[type].items()
                ]
            )
            + "\n\n"
        )

    return pretty


def prompt_dataset_type():
    dataset_types = get_dataset_types(numbered=True)
    min_type = min(dataset_types.keys())
    max_type = max(dataset_types.keys())
    try:
        type_number = int(
            input(
                f"{format_type_list(dataset_types)}Please select the dataset type by number [{min_type} - {max_type}]: "
            )
        )
        dataset_type = dataset_types[type_number]["id"]
    except KeyError:
        logger.error(
            f"Invalid Input. You have to provide a dataset type key between {min_type} and {max_type}."
        )
        exit(1)
    except ValueError:
        logger.error(
            f"Invalid input. You have to provide a number between {min_type} and {max_type}."
        )
    return dataset_type


def run():
    """ run """
    try:
        parser, args = parse_args()

        if not any(vars(args).values()):
            logger.error(
                "No arguments provided. Please use the -h flag to show available parameters."
            )
            sys.exit(2)

        level = logging.WARN
        if args.verbose == 0:
            pass
        elif args.verbose == 1:
            level = logging.INFO
        else:
            level = logging.DEBUG

        FASTGenomicsClient.set_log_level(level)

        if args.action == "lfs-create":
            title = args.title
            if title == "":
                title = "upload " + datetime.datetime.now().strftime(
                    "%d.%m.%Y %H:%M"
                )

            recipient_email = args.recipient_email.lower()  # normalize it

            lfs = FASTGenomicsLargeFileStorageClient()

            zip_password = args.zip_password
            if args.skip_compression:
                assert (
                    len(args.files_or_directory) == 1
                ), "if compression is skipped the it has to be a single file"
                full_path = path.abspath(
                    path.expanduser(args.files_or_directory[0])
                )
                assert path.isfile(
                    full_path
                ), "if compression is skipped the it has to be a single file"
                filename = full_path
            else:
                if zip_password is None or zip_password == "":
                    logging.debug("generating zip password")
                    zip_password = FASTGenomicsClient.generate_password()
                assert (
                    args.zip_filename is not None
                ), "You have to provide a --zip-filename parameter."
                filename = run_zip(
                    args.files_or_directory, args.zip_filename, zip_password
                )

            result = lfs.upload_file_to_lfs(
                args.provider, filename, title, recipient_email, zip_password
            )
            output(result.__dict__)

        elif args.action == "lfs-get-downloadurl":
            lfs = FASTGenomicsLargeFileStorageClient()
            url = lfs.get_download_url(args.id, args.access_token)
            output({"download_url": url})

        elif args.action == "dataset-create":
            if args.title is None:
                args.title = input(
                    f"Please enter the title of the dataset you want to create: "
                )
            if args.title is None or args.title == "":
                args.title = "upload " + datetime.datetime.now().strftime(
                    "%d.%m.%Y %H:%M"
                )
                logger.warning(
                    f'Dataset title automatically set to "{args.title}".'
                )
            if args.dataset_type is None:
                args.dataset_type = prompt_dataset_type()
            client = FASTGenomicsDatasetClient()
            result = client.create_dataset(args.title, args.dataset_type)
            id = result.json()["id"]
            output({"dataset_id": id})

        elif args.action == "dataset-upload":
            results = []
            if args.type == "primarydata":
                args.type = (
                    "expressiondata"  # TODO Change directly in platform API
                )
            if args.id is None:
                args.id = input(
                    f"Please enter the id of the dataset you want to add the file(s) to: "
                )
            if args.id is None or args.id == "":
                raise ValueError("You have to provide a dataset ID.")
            for file in set(args.files):
                logger.info(
                    f"uploading {args.type} file '{file}' to '{args.id}'"
                )
                client = FASTGenomicsDatasetClient()
                result = client.add_file_to_dataset(
                    args.id, file, args.type, show_progress_bar=True
                )
                results.append(result)
            output(results)

        elif args.action == "dataset-set-metadata":
            if args.id is None:
                args.id = input(
                    f"Please enter the id of the dataset you want to set the metadata for: "
                )
            if args.id is None or args.id == "":
                raise ValueError("You have to provide a dataset ID.")
            if args.metadata.startswith("@"):
                filename = args.metadata[1 : len(args.metadata)]
                logger.info(
                    f"setting metadata for dataset '{args.id}' by file '{filename}'"
                )
                with open(filename, "r") as f:
                    data = f.read()
                d = json.loads(data)
            else:
                logger.info(f"setting metadata for dataset '{args.id}'")
                d = json.loads(args.metadata)

            client = FASTGenomicsDatasetClient()
            client.set_metadata(args.id, d)

        elif args.action == "dataset-delete":
            client = FASTGenomicsDatasetClient()
            client.delete_dataset(args.id)

        elif args.action == "get-types":
            types = get_dataset_types()
            output(types)

        elif args.action == "get-type-details":
            if args.id == None:
                args.id = prompt_dataset_type()

            details = get_dset_details(args.id, mode=args.mode)
            output(details)

        elif args.action == "login":
            ToolConfiguration.ensure_config_json()  # ensure the config is created

            if args.user is None:
                args.user = input(f"Please enter your username: ")
            if args.user is None or args.user == "":
                raise ValueError("You have to provide a username.")
            if args.url is None:
                args.url = input(
                    f"Please enter the platform url [e.g. https://beta.fastgenomics.org]: "
                )
            if args.url is None or args.url == "":
                raise ValueError("You have to provide a platform url.")

            if args.passphrase is None:
                args.passphrase = getpass(
                    f"Please enter your passphrase [selected login method: {args.login_method}]: "
                )
            if args.passphrase is None or args.passphrase == "":
                raise ValueError("You have to provide a passphrase.")
            logger.info(f"login {args.user}")
            client = FASTGenomicsClient()
            client.login(
                args.user, args.passphrase, args.login_method, args.url
            )
            output(client.fastgenomics_account.__dict__)

        elif args.action == "logout":
            logger.info("logout")
            client = FASTGenomicsClient()
            client.logout()

        elif args.action == "configure-aws":
            logger.info("configure aws")
            client = FASTGenomicsClient()
            print("Save this account information in a safe place.")
            print(
                "This account information is required by the Comma Soft team to set up your AWS Large File Storage."
            )
            output(client.aws_configure_cloud())

        elif args.action == "version":
            print("Versions:\n")
            output(VERSIONS)
        else:
            raise RuntimeError(f"unknown action '{args.action}'")

    except Exception as err:
        logging.error(err)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    run()
