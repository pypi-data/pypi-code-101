""" This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

Created on Aug 10, 2021

@author: pymancer@gmail.com (polyanalitika.ru)
"""
from box import Box

POSTGRESQL_DIALECT = 'postgresql'
MSSQL_DIALECT = 'mssql'
SQLITE_DIALECT = 'sqlite'

QUERY_KEY = 'query'

NoneType = type(None)

# fmt: off
WRAP = Box({
    "const": {
        "operation": "+",
        "left": "<+",
        "right": "+>"
    },
    "double": {
        "operation": "=",
        "left": "<=",
        "right": "=>"
    },
    "single": {
        "operation": "-",
        "left": "<-",
        "right": "->"
    },
    "lefts": [
        "<+",
        "<=",
        "<-"
    ],
    "rights": [
        "+>",
        "=>",
        "->"
    ],
    "left_escape": "<",
    "right_escape": ">",
    "key_len": 2
}, frozen_box=True)

DIALECTS = Box({
    POSTGRESQL_DIALECT: {
        "cast": {
            "true": "true",
            "false": "false",
            "null": "null"
        },
        "quote": {
            "double": {
                "left": '"',
                "right": '"'
            },
            "single": {
                "left": "'",
                "right": "'"
            }
        }
    },
    MSSQL_DIALECT: {
        "cast": {
            "true": "true",
            "false": "false",
            "null": "null"
        },
        "quote": {
            "double": {
                "left": '[',
                "right": ']'
            },
            "single": {
                "left": "'",
                "right": "'"
            }
        }
    },
    SQLITE_DIALECT: {
        "cast": {
            "true": "1",
            "false": "0",
            "null": "null"
        },
        "quote": {
            "double": {
                "left": '"',
                "right": '"'
            },
            "single": {
                "left": "'",
                "right": "'"
            }
        }
    }
}, frozen_box=True)
# fmt: on
