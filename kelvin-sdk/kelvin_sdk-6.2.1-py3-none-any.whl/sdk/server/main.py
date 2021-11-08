import pathlib
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from ..lib.configs.internal.kelvin_sdk_server import KelvinSDKServerConfigs
from .interface import (
    app,
    appregistry,
    asset,
    asset_type,
    authentication,
    bridge,
    configuration,
    datatype,
    emulation,
    label,
    node,
    report,
    secret,
    workload,
)

# 1 - Construct the supported routers
supported_routers = [
    app.apps_router,
    app.apps_images_router,
    appregistry.router,
    asset.router,
    asset_type.router,
    authentication.router,
    bridge.router,
    configuration.router,
    datatype.router,
    emulation.router,
    label.router,
    node.router,
    report.router,
    secret.router,
    workload.router,
]

# 2 - Initialise the FastAPI object and setup the supported routers
kelvin_server = FastAPI(
    title=KelvinSDKServerConfigs.kelvin_server_title, description=str(KelvinSDKServerConfigs.kelvin_server_description)
)
for router in supported_routers:
    kelvin_server.include_router(router=router)

# 3 - Setup the structure of the FastAPI
current_directory = pathlib.Path(__file__).parent.resolve()
ui_directory = current_directory / KelvinSDKServerConfigs.kelvin_server_structure_ui_dir
templates_directory = ui_directory / KelvinSDKServerConfigs.kelvin_server_structure_templates_dir
static_directory = ui_directory / KelvinSDKServerConfigs.kelvin_server_structure_static_dir

templates = Jinja2Templates(directory=str(templates_directory))
kelvin_server.mount(
    "/static",
    StaticFiles(directory=static_directory),
    name="static",
)


@kelvin_server.get("/", response_class=HTMLResponse, tags=["Landing page"])
async def root(request: Request) -> Any:
    from kelvin.sdk.cli.version import version as _version

    return templates.TemplateResponse("main.html", {"request": request, "version": _version})


@kelvin_server.get("/info", tags=["System Information"])
async def info() -> dict:
    from kelvin.sdk.cli.version import version as _version
    from kelvin.sdk.lib.configs.internal.general_configs import KSDKHelpMessages
    from kelvin.sdk.lib.session.session_manager import session_manager
    from kelvin.sdk.lib.utils.general_utils import get_system_information

    system_information = get_system_information()
    ksdk_configuration = session_manager.get_global_ksdk_configuration()
    current_url = ksdk_configuration.kelvin_sdk.current_url or KSDKHelpMessages.current_session_login
    return {"current_url": current_url, "version": _version, **system_information}


@kelvin_server.get("/version", tags=["Kelvin SDK version"])
async def version() -> dict:
    from kelvin.sdk.cli.version import version as _version

    return {"version": _version}
