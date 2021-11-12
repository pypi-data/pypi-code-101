from enum import Enum
from dataclasses 	import dataclass

class ChannelType(Enum):
    IN = "IN"
    OUT = "OUT"

class ChannelStatusIntegration(Enum):
    SENT_CHANNEL_OUT      = "SENT_TO_CHANNEL_OUT"
    CHANNEL_OUT_APPROVED  = "CHANNEL_OUT_APPROVED"
    CHANNEL_OUT_ERROR     = "CHANNEL_OUT_ERROR"

@dataclass
class ChannelStatus:
	external_id : str
	status	    : ChannelStatusIntegration
	message     : str