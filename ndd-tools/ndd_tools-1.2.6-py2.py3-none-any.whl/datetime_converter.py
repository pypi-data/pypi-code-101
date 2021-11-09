# -*- coding: utf-8 -*-
from typing import Union
from datetime import datetime
from .constants import DATETIME_FORMATS
from dateutil import tz


def get_now_with_tz(zone: str = "Asia/Ho_Chi_Minh", str_format="%Y-%m-%d %H:%M:%S %z") -> str:
    return datetime.utcnow().astimezone(tz.gettz(zone)).strftime(str_format)

def str_to_datetime(target: Union[str, datetime]):
    if isinstance(target, datetime):
        return target
    if isinstance(target, str):
        for datetime_format in DATETIME_FORMATS:
            try:
                return datetime.strptime(target, datetime_format)
            except Exception:
                pass
        raise LookupError('Not match any predefined datetime formats')

    raise ValueError('this function only convert string date to datetime object')
