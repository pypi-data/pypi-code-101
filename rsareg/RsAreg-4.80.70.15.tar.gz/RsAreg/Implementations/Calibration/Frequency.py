from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get_sw_points(self) -> str:
		"""SCPI: CALibration:FREQuency:SWPoints \n
		Snippet: value: str = driver.calibration.frequency.get_sw_points() \n
		No command help available \n
			:return: freq_switch_point: No help available
		"""
		response = self._core.io.query_str('CALibration:FREQuency:SWPoints?')
		return trim_str_response(response)

	def set_sw_points(self, freq_switch_point: str) -> None:
		"""SCPI: CALibration:FREQuency:SWPoints \n
		Snippet: driver.calibration.frequency.set_sw_points(freq_switch_point = '1') \n
		No command help available \n
			:param freq_switch_point: No help available
		"""
		param = Conversions.value_to_quoted_str(freq_switch_point)
		self._core.io.write(f'CALibration:FREQuency:SWPoints {param}')
