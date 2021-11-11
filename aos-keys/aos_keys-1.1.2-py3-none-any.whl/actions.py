#
#  Copyright (c) 2018-2021 Renesas Inc.
#  Copyright (c) 2018-2021 EPAM Systems Inc.
#

import sys
from enum import Enum
from pathlib import Path

from rich.console import Console

from aos_keys.cloud_api import receive_certificate_by_token
from aos_keys.key_manager import generate_pair, save_pkcs_container, generate_pair_rsa, pkcs12_to_pem_bytes

_OEM_FILE_NAME = "aos-user-oem.p12"
_SP_FILE_NAME = "aos-user-sp.p12"


class UserType(Enum):
    SP = 'sp'
    OEM = 'oem'
    ADMIN = 'admin'


def new_token_user(domain: str, output_directory: str, auth_token: str, user_type: UserType, create_ecc_key):
    console = Console()
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    if user_type == UserType.SP.value:
        file_path = Path(output_directory) / _SP_FILE_NAME
    elif user_type == UserType.OEM.value:
        file_path = Path(output_directory) / _OEM_FILE_NAME
    else:
        console.print(f'Unsupported user role!', style='red')
        sys.exit(0)

    if file_path.exists():
        console.print(f'File [{file_path}] exists. Cannot proceed!', style="bold red")

    if create_ecc_key:
        private_key_bytes, csr = generate_pair()
    else:
        private_key_bytes, csr = generate_pair_rsa()

    user_certificate = receive_certificate_by_token(domain, token=auth_token, csr=csr)
    save_pkcs_container(private_key_bytes, user_certificate, file_path)
    console.print(f'Done!', style='green')


def convert_pkcs12_file_to_pem(pkcs12_path: str, output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    console = Console()
    cert_file_name = Path(output_dir) / 'user-certificate.pem'
    key_file_name = Path(output_dir) / 'user-key.pem'

    if not Path(pkcs12_path).exists():
        console.print(f'File [{pkcs12_path}] not found. Cannot proceed!', style="bold red")
        sys.exit(1)

    for file_name in (cert_file_name, key_file_name):
        if file_name.exists():
            console.print(f'Destination file [{file_name}] exists. Cannot proceed!', style="bold red")
            sys.exit(1)

    with open(pkcs12_path, 'rb') as pkcs12_file:
        cert_bytes, key_bytes = pkcs12_to_pem_bytes(pkcs12_file.read())

    with open(cert_file_name, "wb") as cert:
        cert.write(cert_bytes)
        console.print(f'File created: {cert_file_name}!', style='green')

    with open(key_file_name, "wb") as key:
        key.write(key_bytes)
        console.print(f'File created: {key_file_name}!', style='green')

    console.print(f'Done!', style='green')
