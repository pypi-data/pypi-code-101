from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dattenuator:
	"""Dattenuator commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dattenuator", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:DATTenuator:STATe \n
		Snippet: value: bool = driver.source.sweep.power.dattenuator.get_state() \n
		No command help available \n
			:return: data_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:DATTenuator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, data_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:DATTenuator:STATe \n
		Snippet: driver.source.sweep.power.dattenuator.set_state(data_state = False) \n
		No command help available \n
			:param data_state: No help available
		"""
		param = Conversions.bool_to_str(data_state)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:POWer:DATTenuator:STATe {param}')
