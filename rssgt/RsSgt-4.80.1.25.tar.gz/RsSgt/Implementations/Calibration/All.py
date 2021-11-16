from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get_measure(self) -> bool:
		"""SCPI: CALibration:ALL:[MEASure] \n
		Snippet: value: bool = driver.calibration.all.get_measure() \n
		Starts all internal adjustments for which no external measuring equipment is required. \n
			:return: all: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('CALibration:ALL:MEASure?')
		return Conversions.str_to_bool(response)
