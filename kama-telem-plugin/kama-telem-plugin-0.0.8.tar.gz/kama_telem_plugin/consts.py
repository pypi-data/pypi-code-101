from kama_sdk.core.core.consts import KTEA_TYPE_SERVER
from kama_sdk.core.core.types import KteaDict

PLUGIN_ID = 'nmachine.telem'
STRATEGY_KEY = "strategy"
SVC_NAME = 'telem'


PROTOTYPE_MODE_KTEA = KteaDict(
  type=KTEA_TYPE_SERVER,
  version="1.0.0",
  uri="https://api.nmachine.io/ktea/nmachine/telem-plugin"
)
