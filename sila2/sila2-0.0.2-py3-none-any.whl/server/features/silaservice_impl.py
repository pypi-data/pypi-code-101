from __future__ import annotations

from os.path import join
from typing import TYPE_CHECKING, Callable, List

from sila2 import resource_dir
from sila2.framework.errors.defined_execution_error import DefinedExecutionError
from sila2.framework.errors.no_metadata_allowed import NoMetadataAllowed
from sila2.framework.feature import Feature
from sila2.server.features.silaservice_base import SiLAServiceBase

SiLAService = Feature(open(join(resource_dir, "fdl", "SiLAService.sila.xml"), encoding="utf-8").read())
if TYPE_CHECKING:
    from sila2.pb2_stubs import SiLAService_pb2_grpc
    from sila2.server.sila_server import SilaServer

    SiLAService._servicer_cls = SiLAService_pb2_grpc.SiLAServiceServicer


def no_metadata_allowed(func: Callable):
    def wrapper(*args, **kwargs):
        metadata = kwargs.pop("metadata")
        if metadata:
            raise NoMetadataAllowed(f"SiLAService.{func.__name__} received metadata {list(metadata.keys())}")
        return func(*args, **kwargs)

    return wrapper


class UnimplementedFeature(DefinedExecutionError):
    def __init__(self, feature_identifier: str):
        super().__init__(
            SiLAService.defined_execution_errors["UnimplementedFeature"],
            f"The Feature specified by the given Feature identifier {feature_identifier} "
            f"is not implemented by the server.",
        )


class SiLAServiceImpl(SiLAServiceBase):
    parent_server: SilaServer

    def __init__(self, parent_server: SilaServer):
        self.parent_server = parent_server

    @no_metadata_allowed
    def GetFeatureDefinition(self, FeatureIdentifier: str) -> str:
        feature_id = FeatureIdentifier.split("/")[-2]

        if feature_id in self.parent_server.features:
            return self.parent_server.features[feature_id]._feature_definition
        raise UnimplementedFeature(FeatureIdentifier)

    @no_metadata_allowed
    def SetServerName(self, ServerName: str) -> None:
        self.parent_server.server_name = ServerName

    @no_metadata_allowed
    def get_ImplementedFeatures(self) -> List[str]:
        return [f.fully_qualified_identifier for f in self.parent_server.features.values()]

    @no_metadata_allowed
    def get_ServerName(self) -> str:
        return self.parent_server.server_name

    @no_metadata_allowed
    def get_ServerType(self) -> str:
        return self.parent_server.server_type

    @no_metadata_allowed
    def get_ServerUUID(self) -> str:
        return str(self.parent_server.server_uuid)

    @no_metadata_allowed
    def get_ServerDescription(self) -> str:
        return self.parent_server.server_description

    @no_metadata_allowed
    def get_ServerVersion(self) -> str:
        return self.parent_server.server_version

    @no_metadata_allowed
    def get_ServerVendorURL(self) -> str:
        return self.parent_server.server_vendor_url
