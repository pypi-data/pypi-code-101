from typing import (
    Callable,
)

from thirdweb_web3._utils.rpc_abi import (
    RPC,
)
from thirdweb_web3.method import (
    Method,
)
from thirdweb_web3.types import (
    TxPoolContent,
    TxPoolInspect,
    TxPoolStatus,
)

content: Method[Callable[[], TxPoolContent]] = Method(
    RPC.txpool_content,
    mungers=None,
)


inspect: Method[Callable[[], TxPoolInspect]] = Method(
    RPC.txpool_inspect,
    mungers=None,
)


status: Method[Callable[[], TxPoolStatus]] = Method(
    RPC.txpool_status,
    mungers=None,
)
