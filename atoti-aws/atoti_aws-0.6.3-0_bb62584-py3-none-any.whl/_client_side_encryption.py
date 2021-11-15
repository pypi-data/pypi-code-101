from dataclasses import dataclass

from atoti.client_side_encryption import ClientSideEncryption
from atoti.config.key_pair import KeyPairConfig


@dataclass(frozen=True)
class AwsClientSideEncryption:
    region: str
    """The AWS region to interact with."""


@dataclass(frozen=True)
class AwsKmsConfig(AwsClientSideEncryption, ClientSideEncryption):
    key_id: str
    """The ID to identify the key in KMS."""


@dataclass(frozen=True)
class AwsKeyPair(KeyPairConfig, AwsClientSideEncryption, ClientSideEncryption):
    """The key pair to use for client side encryption."""


def create_aws_kms_config(*, region: str, key_id: str) -> ClientSideEncryption:
    """Create the KMS configuration to use for `client side encryption <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__.

    The AWS KMS CMK must have been created in the same AWS region as the destination bucket (Cf. `AWS documentation <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-config-for-kms-objects.html>`__).

    Args:
        region: The AWS region to interact with.
        key_id: The ID to identify the key in KMS.
    """
    return AwsKmsConfig(region=region, key_id=key_id)


def create_aws_key_pair(
    *, region: str, private_key: str, public_key: str
) -> ClientSideEncryption:
    """Create the key pair to use for `client side encryption <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__.

    Args:
        region: The AWS region to interact with.
        private_key: The private key.
        public_key: The public key.
    """
    return AwsKeyPair(region=region, public_key=public_key, private_key=private_key)
