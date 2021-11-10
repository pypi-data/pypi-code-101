from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Operating:
	"""Operating commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("operating", core, parent)

	def get_internal(self) -> float:
		"""SCPI: SENSe:BASE:TEMPerature:OPERating:INTernal \n
		Snippet: value: float = driver.sense.base.temperature.operating.get_internal() \n
		No command help available \n
			:return: temperature: No help available
		"""
		response = self._core.io.query_str('SENSe:BASE:TEMPerature:OPERating:INTernal?')
		return Conversions.str_to_float(response)
