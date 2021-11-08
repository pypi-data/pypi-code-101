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

import re
from functools import total_ordering
from typing import Optional

from packaging.version import Version as _Version
from pydantic import Field, StrictInt, StrictStr

from kelvin.sdk.lib.models.generic import KSDKModel


@total_ordering
class Version(StrictStr):
    regex = re.compile(r"^([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?$")

    def __lt__(self, other: str) -> bool:
        """Less than comparison."""

        return _Version(self) < _Version(other)


class NameDNS(StrictStr):
    regex = re.compile(r"^[a-z]([-a-z0-9]*[a-z0-9])?$")


class Identifier(StrictStr):
    regex = re.compile(r"^[a-zA-Z]\w*$")


class Port(StrictInt):
    gt = 0
    le = 65535


class PythonEntryPoint(StrictStr):
    regex = re.compile(r"^[a-zA-Z]\w*(\.[a-zA-Z]\w*)*(:[a-zA-Z]\w*)?$")


class ZMQUrl(StrictStr):
    regex = re.compile(r"^(tcp://[^:]+:[0-9]+|ipc://.+)$")


class DottedIdentifier(StrictStr):
    regex = re.compile(r"^([a-z][a-z0-9_]*\.)*[a-z][a-z0-9_]*$")


class Name(StrictStr):
    regex = re.compile(r"^[a-z]([-_.a-z0-9]*[a-z0-9])?$")


class EnvironmentVar(KSDKModel):
    name: Identifier = Field(..., description="Environment variable name.", title="Environment Variable Name")
    value: Optional[str] = Field(None, description="Environment variable value.", title="Environment Variable Value")
