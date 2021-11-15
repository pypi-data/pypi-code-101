from pathlib import Path
from typing import Optional

from atoti._plugins import Plugin
from atoti.query.session import QuerySession
from atoti.session import Session

from ._client_side_encryption import create_azure_key_pair

JAR_PATH = (Path(__file__).parent / "data" / "atoti-azure.jar").absolute()


class AzurePlugin(Plugin):
    """Azure plugin."""

    def static_init(self):
        """Init to be called only once."""

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return JAR_PATH

    def init_session(self, session: Session):
        """Initialize the session."""
        if (
            session._config.azure is not None
            and session._config.azure.client_side_encryption is not None
            and session._config.azure.client_side_encryption.key_pair
        ):
            session._set_client_side_encryption(
                create_azure_key_pair(
                    key_id=session._config.azure.client_side_encryption.key_pair.key_id,
                    private_key=session._config.azure.client_side_encryption.key_pair.private_key,
                    public_key=session._config.azure.client_side_encryption.key_pair.public_key,
                )
            )
        session._java_api.gateway.jvm.io.atoti.loading.azure.AzurePlugin.init()  # type: ignore

    def init_query_session(self, query_session: QuerySession):
        """Initialize the query session."""
