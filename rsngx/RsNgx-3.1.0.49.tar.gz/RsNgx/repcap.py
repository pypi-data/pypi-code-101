from enum import Enum
# noinspection PyPep8Naming
from .Internal.RepeatedCapability import VALUE_DEFAULT as DefaultRepCap
# noinspection PyPep8Naming
from .Internal.RepeatedCapability import VALUE_EMPTY as EmptyRepCap


# noinspection SpellCheckingInspection
class Channel(Enum):
	"""Repeated capability Channel"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4


# noinspection SpellCheckingInspection
class DigitalIo(Enum):
	"""Repeated capability DigitalIo"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8
