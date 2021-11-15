from pathlib import Path
from typing import Optional

from atoti._plugins import Plugin
from atoti.query.session import QuerySession
from atoti.session import Session

from ._client_side_encryption import create_aws_key_pair, create_aws_kms_config

JAR_PATH = (Path(__file__).parent / "data" / "atoti-aws.jar").absolute()


class AWSPlugin(Plugin):
    """AWS plugin."""

    def static_init(self):
        """Init to be called only once."""

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return JAR_PATH

    def init_session(self, session: Session):
        """Initialize the session."""
        if (
            session._config.aws is not None
            and session._config.aws.client_side_encryption is not None
        ):
            if session._config.aws.client_side_encryption.kms is not None:
                session._set_client_side_encryption(
                    create_aws_kms_config(
                        region=session._config.aws.region,
                        key_id=session._config.aws.client_side_encryption.kms.key_id,
                    )
                )
            if session._config.aws.client_side_encryption.key_pair is not None:
                session._set_client_side_encryption(
                    create_aws_key_pair(
                        region=session._config.aws.region,
                        private_key=session._config.aws.client_side_encryption.key_pair.private_key,
                        public_key=session._config.aws.client_side_encryption.key_pair.public_key,
                    )
                )
        session._java_api.gateway.jvm.io.atoti.loading.s3.AwsPlugin.init()  # type: ignore

    def init_query_session(self, query_session: QuerySession):
        """Initialize a query session."""
