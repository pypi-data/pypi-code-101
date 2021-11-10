from typing import Generator

from fastapi import Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from crud import crud
from models import models
from models.user import LoginActivity
from schemas import schemas
from core import security
from core.config import settings
from db.session import SessionLocal
from starlette.requests import Request
from ua_parser import user_agent_parser

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def login_activity_from_request(*, request: Request):
    user_agent = user_agent_parser.Parse(request.headers.get('user-agent'))
    os = user_agent['os']['family'].replace("None", '')
    browser = user_agent['user_agent']['family'].replace("None", '')
    browser_version = f"{user_agent['user_agent']['major']}.{user_agent['user_agent']['minor']}.{user_agent['user_agent']['patch']}".replace(
        "None", '')

    return LoginActivity(platform=os, browser=browser + ':' + browser_version, user_ip=request.client.host)


def get_current_user_token(
        db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload['user_data'])

    except (jwt.JWTError, ValidationError, Exception) as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return token


def get_current_user(
        db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload['user_data'])


    except (jwt.JWTError, ValidationError) as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    user = crud.user.get_available(db, id=token_data.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
        current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_admin(
        current_user: models.User = Depends(get_current_user),
) -> models.User:
    if current_user.group is not None and current_user.group.name in ['superuser', 'admin']:
        return current_user
    # if not crud.user.is_superuser(current_user):
    raise HTTPException(
        status_code=403, detail="The user doesn't have enough privileges"
    )


def get_site_origin(site_origin: str = Header(...)):
    return site_origin
