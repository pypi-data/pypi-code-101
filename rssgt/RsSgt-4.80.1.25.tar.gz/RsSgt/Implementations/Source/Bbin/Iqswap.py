from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iqswap:
	"""Iqswap commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqswap", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BBIN:IQSWap:[STATe] \n
		Snippet: value: bool = driver.source.bbin.iqswap.get_state() \n
		This command swaps the I and Q channel if set to ON. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:IQSWap:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:IQSWap:[STATe] \n
		Snippet: driver.source.bbin.iqswap.set_state(state = False) \n
		This command swaps the I and Q channel if set to ON. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:IQSWap:STATe {param}')
