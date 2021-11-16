from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Swap:
	"""Swap commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("swap", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:SWAP:[STATe] \n
		Snippet: value: bool = driver.source.iq.impairment.swap.get_state() \n
		When set to ON, this command swaps the I and Q channel for an external modulation signal. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:IMPairment:SWAP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:SWAP:[STATe] \n
		Snippet: driver.source.iq.impairment.swap.set_state(state = False) \n
		When set to ON, this command swaps the I and Q channel for an external modulation signal. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:IMPairment:SWAP:STATe {param}')
