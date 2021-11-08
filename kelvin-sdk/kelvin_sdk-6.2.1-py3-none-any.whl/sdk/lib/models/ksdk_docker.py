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

from datetime import datetime
from typing import List, Optional, Tuple

from pydantic import Field

from kelvin.sdk.lib.models.generic import KPath, KSDKModel
from kelvin.sdk.lib.models.types import BaseEnum


class KSDKDockerVolume(KSDKModel):
    source_file_path: KPath  # e.g. /anything/regardless/of/operative_system/mosquitto.conf
    container_file_path: str  # e.g. /mosquitto/config/mosquitto.conf - linux
    content: str


class KSDKNetworkConfig(KSDKModel):
    network_name: str
    network_driver: str


class KSDKDockerAuthentication(KSDKModel):
    registry_url: str
    registry_port: str
    username: str
    password: str

    @property
    def full_registry_url(self) -> str:
        return f"{self.registry_url}:{self.registry_port}"


class DockerPort(KSDKModel):
    port_type: str = Field(None, alias="Type")
    private_port: str = Field(None, alias="PrivatePort")
    public_port: str = Field(None, alias="PublicPort")

    @property
    def port_mapping(self) -> str:
        return f"{self.port_type}:{self.private_port}->{self.public_port}"

    def __repr__(self) -> str:
        return self.port_mapping


class DockerMount(KSDKModel):
    mount_type: str = Field(None, alias="Type")
    source: str = Field(None, alias="Source")
    destination: str = Field(None, alias="Destination")
    mode: str = Field(None, alias="Mode")
    rw: str = Field(None, alias="RW")
    bind_propagation: str = Field(None, alias="Propagation")

    @property
    def pretty_display_format(self) -> str:
        from kelvin.sdk.lib.utils.display_utils import pretty_colored_content

        return pretty_colored_content(content=self.dict())


class DockerContainer(KSDKModel):
    # 1 - raw content
    raw_content: Optional[dict] = {}
    # 2 - internal fields
    id: str
    container_names: Optional[List[str]] = []
    image_name: str
    running: bool = False
    status: str = "N/A"
    labels: Optional[dict] = {}
    ip_address: Optional[str]  # overall ip address
    mounts: Optional[List[DockerMount]] = []
    ports: List[DockerPort] = []

    @property
    def container_status_for_display(self) -> str:
        is_running: str = "Running" if self.running else "Not Running"
        return f"{is_running} - {self.status}"

    @property
    def container_ports_for_display(self) -> str:
        result = ""
        if self.ports:
            result = "\n".join(list(set([item.port_mapping for item in self.ports])))
        return result

    @property
    def container_mounts_for_display(self) -> str:
        result = ""
        if self.mounts:
            result = "\n".join([item.pretty_display_format for item in self.mounts])
        return result


class DockerImage(KSDKModel):
    id: str
    parent_id: str
    tags: List[str]
    created: int
    labels: Optional[dict]

    @property
    def readable_created_date(self) -> str:
        value = datetime.fromtimestamp(self.created)
        return f"{value:%Y-%m-%d %H:%M:%S}"


class DockerImageNameDetails(KSDKModel):
    registry_url: str
    docker_image_name: str

    @property
    def repository_docker_image_name(self) -> str:
        image, version = self.image_name_and_version
        return f"{self.registry_url}/{image}:{version}"

    @property
    def exclude_registry(self) -> str:
        if "/" in self.docker_image_name:
            extra_url, docker_image = self.docker_image_name.rsplit("/", 1)
            self.docker_image_name = docker_image
        return self.docker_image_name

    @property
    def image_name_and_version(self) -> Tuple[str, str]:
        docker_image_name = self.exclude_registry
        if ":" in docker_image_name:
            image, version = docker_image_name.rsplit(":", 1)
        else:
            image, version = docker_image_name, "latest"

        return image, version

    @property
    def container_name(self) -> str:
        name, _ = self.image_name_and_version
        return f"{name}.app"


class DockerNetwork(KSDKModel):
    name: str = Field(None, alias="Name")
    id: str = Field(None, alias="Id")
    driver: str = Field(None, alias="Driver")
    created: str = Field(None, alias="Created")


class DockerBuildEntry(KSDKModel):
    stream: Optional[str]
    error: Optional[str] = None
    message: Optional[str] = None

    @property
    def stream_content(self) -> Optional[str]:
        return self.stream.strip() if self.stream and "\n" != self.stream else None

    @property
    def error_content(self) -> Optional[str]:
        return self.error.strip() if self.error and "\n" != self.error else None

    @property
    def message_content(self) -> Optional[str]:
        return self.message.strip() if self.message and "\n" != self.error else None

    @property
    def entry_has_errors(self) -> bool:
        has_error = self.error_content is not None or self.message_content is not None
        return has_error

    @property
    def log_content(self) -> str:
        stream_content = self.stream_content or ""
        error_content = self.error_content
        message_content = self.message_content
        stream_content += f"/{error_content}" if error_content else ""
        stream_content += f"/{message_content}" if message_content else ""
        return stream_content


class DockerProgressDetail(KSDKModel):
    current: Optional[int] = 0
    total: Optional[int] = 0


class DockerProgressStatus(BaseEnum):
    PULL_LAYER = "Pulling fs layer"
    DEFAULT = "Default"
    PREPARING = "Preparing"
    PUSHING = "Pushing"
    DOWNLOADING = "Downloading"


class DockerProgressEntry(KSDKModel):
    id: Optional[str]
    status: Optional[str]
    progress: Optional[str]
    progressDetail: Optional[DockerProgressDetail]  # noqa


class AppRunningContainers(KSDKModel):
    existing_images: List[DockerImage] = []
    existing_containers: List[DockerContainer] = []
