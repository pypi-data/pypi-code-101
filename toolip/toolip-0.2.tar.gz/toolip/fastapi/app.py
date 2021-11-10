from secrets import compare_digest

from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from .config import conf
from .constants import DOCS_PATH, OPENAPI_PATH, REDOC_PATH

security = HTTPBasic()


def doc_login(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = compare_digest(credentials.username, conf.doc_username)
    correct_password = compare_digest(credentials.password, conf.doc_password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return


def docs_behind_basic_auth(app: FastAPI, prefix: str = '') -> None:
    errors = [
        attr for attr in ['docs_url', 'redoc_url', 'openapi_url'] if getattr(app, attr) is not None
    ]
    if errors:
        raise ValueError(
            f'The following attributes must be set to None '
            f'when creating the FastAPI app: {", ".join(errors)}'
        )
    router = APIRouter()

    @router.get(OPENAPI_PATH, include_in_schema=False)
    async def get_open_api_endpoint():
        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
        )
        return JSONResponse(openapi_schema)

    app.openapi_url = f'{prefix}{OPENAPI_PATH}'

    @router.get(DOCS_PATH, include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(openapi_url=app.openapi_url, title=app.title + " - Swagger UI")

    @router.get(str(app.swagger_ui_oauth2_redirect_url), include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    @router.get(REDOC_PATH, include_in_schema=False)
    async def redoc_html() -> HTMLResponse:
        return get_redoc_html(openapi_url=str(app.openapi_url), title=app.title + " - ReDoc")

    app.include_router(router, prefix=prefix, dependencies=[Depends(doc_login)])
