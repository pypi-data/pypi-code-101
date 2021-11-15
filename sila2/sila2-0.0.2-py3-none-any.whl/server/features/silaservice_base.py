from abc import ABC, abstractmethod
from typing import Any, Dict, List

from sila2.framework.fully_qualified_identifier import FullyQualifiedIdentifier
from sila2.server.feature_implementation_base import FeatureImplementationBase


class SiLAServiceBase(FeatureImplementationBase, ABC):
    @abstractmethod
    def GetFeatureDefinition(self, FeatureIdentifier: str, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> str:
        pass

    @abstractmethod
    def SetServerName(self, ServerName: str, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> None:
        pass

    @abstractmethod
    def get_ImplementedFeatures(self, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> List[str]:
        pass

    @abstractmethod
    def get_ServerName(self, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> str:
        pass

    @abstractmethod
    def get_ServerType(self, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> str:
        pass

    @abstractmethod
    def get_ServerUUID(self, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> str:
        pass

    @abstractmethod
    def get_ServerDescription(self, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> str:
        pass

    @abstractmethod
    def get_ServerVersion(self, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> str:
        pass

    @abstractmethod
    def get_ServerVendorURL(self, *, metadata: Dict[FullyQualifiedIdentifier, Any]) -> str:
        pass
