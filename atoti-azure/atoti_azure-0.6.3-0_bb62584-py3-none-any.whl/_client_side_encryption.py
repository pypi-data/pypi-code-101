from dataclasses import dataclass

from atoti.client_side_encryption import ClientSideEncryption
from atoti.config.key_pair import KeyPairConfig


@dataclass(frozen=True)
class AzureKeyPair(KeyPairConfig, ClientSideEncryption):
    key_id: str
    """The ID of the key used to encrypt the blob."""


def create_azure_key_pair(
    *, key_id: str, private_key: str, public_key: str
) -> ClientSideEncryption:
    """Create the key pair to use for client side encryption.

    Warning:

        Each encrypted blob must have the metadata attribute ``unencrypted_content_length`` with the unencrypted file size.
        If this is not set, an :guilabel:`Issue while downloading` error will occur.

    Args:
        key_id: The ID of the key used to encrypt the blob.
        private_key: The private key.
        public_key: The public key.
    """
    return AzureKeyPair(key_id=key_id, private_key=private_key, public_key=public_key)
