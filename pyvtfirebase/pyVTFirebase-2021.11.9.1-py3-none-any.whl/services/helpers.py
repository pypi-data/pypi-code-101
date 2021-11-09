import json
import datetime

from pyVTFirebase.services.firestore.types.query import Query
from typing import Union


def build_url(*args, delimiter: str = None) -> str:

    url = ""

    for _i, _sub in enumerate(args):
        if _sub is not None:
            if isinstance(_sub, str):
                if _i != len(args) - 1:
                    url += _sub + "/"
                else:
                    url += _sub
            else:
                raise ValueError("Argument is not of type string")

    if delimiter:
        url += f":{delimiter}"

    return url


def build_params(**kwargs) -> dict:

    params = {}

    for _key in kwargs:
        if kwargs.get(_key) is not None:
            _keyResults = kwargs.get(_key)
            if isinstance(_keyResults, dict):
                for internalKey in _keyResults:
                    if _key == "currentDocument":
                        params[f"currentDocument.{internalKey}"] = _keyResults.get(internalKey)
            else:
                if _key in ["mask", "updateMask"]:
                    _key += ".fieldPaths"

                params[_key] = _keyResults

    return params


def validate_json(*args: dict):
    for _sub in args:
        try:
            if isinstance(_sub, dict):
                return json.loads(json.dumps(_sub))
            else:
                raise ValueError(f"Passed value must be of type {type({})} not {type(_sub)}")
        except Exception as e:
            raise ValueError(f"Invalid json: {e}")


def build_body(**kwargs) -> dict:

    data = {}

    for _key in kwargs:
        if _key == "mask":
            if isinstance(kwargs.get(_key), list):
                data[_key] = {
                    "fieldPaths": kwargs.get(_key)
                }
        elif _key == "documents":
            if isinstance(kwargs.get(_key), list):
                data[_key] = kwargs.get(_key)
        elif _key == "readTime":
            if isinstance(kwargs.get(_key), int):
                if 0 <= kwargs.get(_key) <= 269:
                    data[_key] = _currentTime(minus=kwargs.get(_key))
                else:
                    raise ValueError("readTime not within limits of 0 <= readTime <= 269")

    return data


def _currentTime(minus: int = None) -> str:
    time = datetime.datetime.now(datetime.timezone.utc)

    if minus:
        if 0 <= minus <= 269:
            time -= datetime.timedelta(seconds=minus)
        else:
            raise ValueError(f"Time calculation value supplied: {minus} not within limits 0 <= value <= 269")

    time.isoformat()
    return time.strftime('%Y-%m-%dT%H:%M:%SZ')
