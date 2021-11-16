from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bband:
	"""Bband commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bband", core, parent)

	def get_state(self) -> bool:
		"""SCPI: CALibration:IQModulator:BBANd:[STATe] \n
		Snippet: value: bool = driver.calibration.iqModulator.bband.get_state() \n
		No command help available \n
			:return: modulator: OFF| ON| 1| 0
		"""
		response = self._core.io.query_str('CALibration:IQModulator:BBANd:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, modulator: bool) -> None:
		"""SCPI: CALibration:IQModulator:BBANd:[STATe] \n
		Snippet: driver.calibration.iqModulator.bband.set_state(modulator = False) \n
		No command help available \n
			:param modulator: OFF| ON| 1| 0
		"""
		param = Conversions.bool_to_str(modulator)
		self._core.io.write(f'CALibration:IQModulator:BBANd:STATe {param}')
