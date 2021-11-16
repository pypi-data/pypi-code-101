# -*- coding: utf-8 -*-
import json

AUTH_ERROR = {
    "error_code": 10011,
    "msg": "auth fail"
}

PARAM_ERROR = {
    "error_code": 10012,
    "msg": "param error"
}

def http_status_error(r):
    return {
        "error_code": r.status_code
    }