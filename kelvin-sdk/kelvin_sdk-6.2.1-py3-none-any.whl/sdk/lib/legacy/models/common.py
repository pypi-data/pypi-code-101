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

import re
from typing import Optional

from pydantic import Field, StrictInt, StrictStr

from kelvin.sdk.lib.models.generic import KSDKModel


class DottedIdentifier(StrictStr):
    regex = re.compile(r"^[a-zA-Z]\w*(\.[a-zA-Z]\w*)*$")


class PythonEntryPoint(StrictStr):
    regex = re.compile(r"^[a-zA-Z]\w*(\.[a-zA-Z]\w*)*:[a-zA-Z]\w*$")


class Version(StrictStr):
    pass


class DockerImageRef(StrictStr):
    regex = re.compile(r"^([^:]+(:\d+)?/)?[^:]+:[^:]+$")


class Name(StrictStr):
    regex = re.compile(r"^[a-zA-Z][a-zA-Z0-9-]*$")


class Identifier(StrictStr):
    regex = re.compile(r"^[a-zA-Z]\w*$")


class CPU(StrictStr):
    regex = re.compile(r"^[0-9](\.[0-9]+)?(m|)$")


class Port(StrictInt):
    gt = 0
    le = 65535


class OPCUAEndpoint(StrictStr):
    regex = re.compile(r"^opc\.tcp://.+$")


class MQTTURI(StrictStr):
    regex = re.compile(r"^mqtts?://.+$")


class DockerImageName(StrictStr):
    regex = re.compile(r"^([^:]+(:\d+)?/)?[^:]+")


class EnvironmentVar(KSDKModel):
    name: Identifier = Field(..., description="Environment variable name.", title="Environment Variable Name")
    value: Optional[str] = Field(None, description="Environment variable value.", title="Environment Variable Value")


class ZMQUrl(StrictStr):
    regex = re.compile(r"^(tcp://[^:]+:[0-9]+|ipc://.+)$")
