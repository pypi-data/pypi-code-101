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

from fastapi import Body

from kelvin.sdk.lib.models.operation import OperationResponse
from kelvin.sdk.server.models.router import KelvinSDKServerRouter

router = KelvinSDKServerRouter(
    prefix="/configurations",
    tags=["Kelvin Usage Configurations - [kelvin configuration]"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def global_configuration_list(should_display: bool = False) -> OperationResponse:
    """
    List all available configurations for the Kelvin-SDK.
    """
    from kelvin.sdk.interface import global_configuration_list as _global_configuration_list

    return _global_configuration_list(should_display=should_display)


@router.post("/set")
def global_configuration_set(config: str = Body(...), value: str = Body(...)) -> OperationResponse:
    """
    Set the specified configuration on the platform system.
    """
    from kelvin.sdk.interface import global_configuration_set as _global_configuration_set

    return _global_configuration_set(configuration=config, value=value)


@router.post("/unset")
def global_configuration_unset(configuration: str = Body(...)) -> OperationResponse:
    """
    Unset the specified configuration from the platform system.
    """
    from kelvin.sdk.interface import global_configuration_unset as _global_configuration_unset

    return _global_configuration_unset(configuration=configuration)
