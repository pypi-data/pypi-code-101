from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def get_temperature(self) -> str:
		"""SCPI: CALibration:LEVel:TEMPerature \n
		Snippet: value: str = driver.calibration.level.get_temperature() \n
		Queries the delta temperature since the last performed adjustment. \n
			:return: temperature: string
		"""
		response = self._core.io.query_str('CALibration:LEVel:TEMPerature?')
		return trim_str_response(response)

	def get_measure(self) -> bool:
		"""SCPI: CALibration:LEVel:[MEASure] \n
		Snippet: value: bool = driver.calibration.level.get_measure() \n
		Starts all adjustments which affect the level. \n
			:return: level: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('CALibration:LEVel:MEASure?')
		return Conversions.str_to_bool(response)
