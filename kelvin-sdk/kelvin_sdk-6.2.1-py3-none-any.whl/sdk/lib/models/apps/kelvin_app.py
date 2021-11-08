"""
Copyright 2021 Kelvin Inc.

Licensed under the Kelvin Inc. Developer SDK License Agreement (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

http://www.kelvininc.com/developer-sdk-license

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional, Tuple

from pydantic import Extra, Field

from kelvin.sdk.lib.models.apps.common import DottedIdentifier, Name, NameDNS, Port, PythonEntryPoint, Version
from kelvin.sdk.lib.models.generic import KPath, KSDKModel
from kelvin.sdk.lib.models.types import BaseEnum
from kelvin.sdk.lib.utils.general_utils import get_requirements_from_file

try:
    from typing import Literal
except ImportError:  # pragma: no cover
    from typing_extensions import Literal  # type: ignore

if TYPE_CHECKING:
    from kelvin.sdk.lib.models.apps.ksdk_app_configuration import ApplicationFlavour


class Images(KSDKModel):
    runner: Optional[str] = Field(None, description="Runner image.", title="Runner Image")
    builder: Optional[str] = Field(None, description="Builder image.", title="Builder Image")


class ApplicationLanguage(BaseEnum):
    python = "python"  # default

    def get_extension(self) -> str:
        return {ApplicationLanguage.python: ".py"}[self]


class PythonLanguageType(KSDKModel):
    class Config:
        extra = Extra.allow

    entry_point: PythonEntryPoint
    requirements: Optional[str] = Field("requirements.txt", description="Package requirements", title="Requirements")
    version: Optional[Literal["3.7", "3.8"]] = Field(None, description="Python version.", title="Python Version")
    flavour: str = Field("default", description="Python application flavour", title="Application Flavour")

    @property
    def app_file_system_name(self) -> str:
        # extract file path from entrypoint point
        if self.entry_point:
            entrypoint_file = self.entry_point.split(":")[0]
            # get parent folder from entrypoint
            return KPath(entrypoint_file)

        return ""

    def get_flavour(self) -> "ApplicationFlavour":
        from kelvin.sdk.lib.models.apps.ksdk_app_configuration import ApplicationFlavour

        return ApplicationFlavour[self.flavour]

    def requirements_file_path(self, app_dir_path: KPath) -> Optional[KPath]:
        """
        When provided with an application dir, yield the complete requirements.txt absolute file path

        Parameters
        ----------
        app_dir_path : KPath
            the application's directory path

        Returns
        -------
        KPath
            the complete path to the requirements.txt file considering the application's directory.

        """
        if self.requirements:
            return (app_dir_path / self.requirements).expanduser().absolute()
        return None

    def requirements_available(self, app_dir_path: KPath) -> Tuple[bool, Optional[KPath]]:
        """
        Indicates whether requirements are available within the requirements.txt file

        Parameters
        ----------
        app_dir_path : KPath
            the application's directory path

        Returns
        -------
        Tuple[bool, Optional[KPath]]
            A tuple containing (left) a bool indicating there are requirements and (right) the path to the file

        """
        requirements_file_path = self.requirements_file_path(app_dir_path=app_dir_path)
        if requirements_file_path:
            return bool(get_requirements_from_file(file_path=requirements_file_path)), requirements_file_path
        return False, None


class Credentials(KSDKModel):
    username: str
    password: str


class Authentication(KSDKModel):
    type: str
    credentials: Credentials


class Mqtt(KSDKModel):
    ip: str = Field(..., description="MQTT Broker IP address.", title="IP")
    port: Port = Field(..., description="MQTT Broker Port.", title="Port")
    authentication: Optional[Authentication] = Field(
        None, description="MQTT Broker Authentication Settings.", title="Authentication"
    )

    @staticmethod
    def default_mqtt_configuration(ip_address: str) -> dict:
        return Mqtt(
            ip=ip_address,
            port=1883,
            authentication=Authentication(
                type="credentials", credentials=Credentials(username="kelvin", password="kelvin")  # nosec
            ),
        ).dict()  # nosec


class Language(KSDKModel):
    type: ApplicationLanguage = Field(..., description="Language type.", title="Language Type")
    python: Optional[PythonLanguageType] = None


class InterfaceDescriptorType(BaseEnum):
    serial = "serial"
    ethernet = "ethernet"
    file = "file"


class DataType(KSDKModel):
    name: DottedIdentifier = Field(..., description="Data type name.", title="Data Type Name")
    version: Version = Field(..., description="Data type version.", title="Data Type Version")
    path: Optional[str] = Field(None, description="Data type path.", title="Data Type Path")

    @property
    def name_with_version(self) -> str:
        return f"{self.name}:{self.version}"


class Item(KSDKModel):
    name: DottedIdentifier = Field(..., description="Item name.", title="Item name")
    value: Any = Field(..., description="Item value.", title="Item value")


class IO(KSDKModel):
    name: DottedIdentifier = Field(..., description="Input/Output name.", title="Input/Output name")
    data_type: DottedIdentifier = Field(None, description="Data type name.", title="Data Type Name")
    values: List[Item] = []


class MetricInfo(KSDKModel):
    node_names: Optional[List[NameDNS]] = Field(None, description="List of Node names.", title="Node Names")
    workload_names: Optional[List[NameDNS]] = Field(None, description="List of Workload names.", title="Workload Names")
    asset_names: Optional[List[Name]] = Field(None, description="List of asset names.", title="Asset Names")
    names: Optional[List[Name]] = Field(None, description="List of external metric names.", title="Names")


class Metric(KSDKModel):
    name: Name = Field(..., description="Name.", title="Name")
    data_type: str = Field(..., description="Data type.", title="Data Type")
    sources: Optional[List[MetricInfo]] = None
    targets: Optional[List[MetricInfo]] = None


class KelvinAppType(KSDKModel):
    images: Optional[Images] = Field(
        None, description="Image configuration for building a Kelvin application.", title="Kelvin Application Images"
    )
    system_packages: Optional[List[str]] = Field(
        None, description="Packages to install into image.", title="System Packages"
    )
    mqtt: Optional[Mqtt] = None
    language: Language
    data_types: Optional[List[DataType]] = []
    inputs: Optional[List[Metric]] = Field(None, description="Inputs.", title="Inputs")
    outputs: Optional[List[Metric]] = Field(None, description="Outputs.", title="Outputs")
    configuration: Optional[Any] = Field(None, description="Configuration.", title="Configuration")
