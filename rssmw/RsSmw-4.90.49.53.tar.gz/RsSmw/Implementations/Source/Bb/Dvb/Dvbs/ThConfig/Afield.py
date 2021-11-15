from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Afield:
	"""Afield commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("afield", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:AFIeld:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.thConfig.afield.get_state() \n
		Inserts an adaptation field in the packet. \n
			:return: afield: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:THConfig:AFIeld:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, afield: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:AFIeld:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbs.thConfig.afield.set_state(afield = False) \n
		Inserts an adaptation field in the packet. \n
			:param afield: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(afield)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:THConfig:AFIeld:STATe {param}')
