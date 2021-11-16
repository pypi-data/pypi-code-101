import dataclasses
from typing import Literal

from shopify_client.script_tag.constants import ScriptTagDisplayScope


@dataclasses.dataclass
class ScriptTagInput:
    src: str
    cache: bool = False
    display_scope: Literal[
        ScriptTagDisplayScope.ALL,
        ScriptTagDisplayScope.ONLINE_STORE,
        ScriptTagDisplayScope.ORDER_STATUS
    ] = ScriptTagDisplayScope.ALL
