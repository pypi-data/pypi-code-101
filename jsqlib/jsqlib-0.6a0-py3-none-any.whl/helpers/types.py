""" This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

Created on Aug 14, 2021

@author: pymancer@gmail.com (polyanalitika.ru)
"""
from typing import Union
from typing_extensions import TypeAlias

BL_T: TypeAlias = Union[bool, list]
LD_T: TypeAlias = Union[dict, list]
SI_T: TypeAlias = Union[str, int]
SD_T: TypeAlias = Union[str, dict]
SIB_T: TypeAlias = Union[SI_T, bool]
SID_T: TypeAlias = Union[SI_T, dict]
SDB_T: TypeAlias = Union[str, dict, bool]
SIBD_T: TypeAlias = Union[SIB_T, dict]
SIBN_T: TypeAlias = Union[SIB_T, None]
SIBNL_T: TypeAlias = Union[SIBN_T, list]
SIBND_T: TypeAlias = Union[SIBN_T, dict]
SIBNLD_T: TypeAlias = Union[SIBNL_T, dict]
