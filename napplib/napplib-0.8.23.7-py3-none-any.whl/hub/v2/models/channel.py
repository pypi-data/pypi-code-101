from enum import Enum
from dataclasses 	import dataclass

class ChannelType(Enum):
    IN = "IN"
    OUT = "OUT"

@dataclass
class ChannelStatus:
	external_id : str
	status	    : str
	message     : str