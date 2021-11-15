from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Payload:
	"""Payload commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("payload", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:PAYLoad:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.thConfig.payload.get_state() \n
		Adds a payload field in packet. \n
			:return: payload: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:THConfig:PAYLoad:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, payload: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:THConfig:PAYLoad:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbs.thConfig.payload.set_state(payload = False) \n
		Adds a payload field in packet. \n
			:param payload: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(payload)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:THConfig:PAYLoad:STATe {param}')
