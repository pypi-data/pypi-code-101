from enum import Enum
from typing import Optional

from pydantic import BaseSettings


class EnvironmentEnum(str, Enum):
    production = 'production'
    development = 'development'
    test = 'test'  # for pytest
    qa = 'qa'


class SentryEnvironment(str, Enum):
    production = 'production'
    staging = 'staging'


class MainConfiguration(BaseSettings):
    environment: EnvironmentEnum = EnvironmentEnum.development
    sentry_environment: Optional[SentryEnvironment] = None
    '''
    Sentry URL to server project, including key
    https://docs.sentry.io/error-reporting/configuration/
    '''
    sentry_dsn: str = ''

    @property
    def in_test(self) -> bool:
        return self.environment == EnvironmentEnum.test

    @property
    def in_production(self) -> bool:
        return self.environment == EnvironmentEnum.production
