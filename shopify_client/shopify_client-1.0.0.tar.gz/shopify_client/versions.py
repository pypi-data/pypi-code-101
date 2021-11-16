from enum import Enum


class APIVersion(Enum):
    APRIL_2021 = '2021-04'
    OCTOBER_2021 = '2021-10'


BASE_VERSION = APIVersion.OCTOBER_2021.value
