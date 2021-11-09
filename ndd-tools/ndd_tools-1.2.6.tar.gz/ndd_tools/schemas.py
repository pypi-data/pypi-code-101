from sys import flags
from pydantic import BaseModel
import enum
from typing import List, Dict, Optional, Any

# -------------------------------------------------
#   For Boring Regex
#
class EnumStrategy(enum.Enum):
    MATCH = 'match'
    SEARCH = 'search'
    FINDALL = 'findall'
    FINDITER = 'finditer'
    GETALL = 'getall'


class EnumGroupType(enum.Enum):
    GROUP = "group"
    GROUPS = "groups"
    GROUPDICT = "groupdict"

class ObjFieldPatternRegexConfig(BaseModel):
    value: str
    group_type: EnumGroupType
    group_indexes: int


class ObjFieldRegexConfig(BaseModel):
    active: bool = True
    field: List[Any]
    key: str
    strategy: EnumStrategy
    patterns: List[ObjFieldPatternRegexConfig]


class ObjectRegexConfig(BaseModel):
    result_keys: List[str]
    regex_fields: List[ObjFieldRegexConfig]


class RegexExecutorConfig(BaseModel):
    version: str
    name: str
    description: str
    author: Optional[str]
    config: Dict[str, ObjectRegexConfig]


class RegexKeyResult(BaseModel):
    result: Any
    source: Optional[str]
    strategy: EnumStrategy