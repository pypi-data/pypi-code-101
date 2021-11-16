from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stuffing:
	"""Stuffing commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stuffing", core, parent)

	def get_low(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:STUFfing:LOW \n
		Snippet: value: bool = driver.source.bb.dvbt.stuffing.get_low() \n
		Activates stuffing. \n
			:return: stuffing_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:STUFfing:LOW?')
		return Conversions.str_to_bool(response)

	def set_low(self, stuffing_lp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:STUFfing:LOW \n
		Snippet: driver.source.bb.dvbt.stuffing.set_low(stuffing_lp = False) \n
		Activates stuffing. \n
			:param stuffing_lp: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(stuffing_lp)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:STUFfing:LOW {param}')

	def get_high(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:STUFfing:[HIGH] \n
		Snippet: value: bool = driver.source.bb.dvbt.stuffing.get_high() \n
		Activates stuffing. \n
			:return: stuffing_hp: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:STUFfing:HIGH?')
		return Conversions.str_to_bool(response)

	def set_high(self, stuffing_hp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:STUFfing:[HIGH] \n
		Snippet: driver.source.bb.dvbt.stuffing.set_high(stuffing_hp = False) \n
		Activates stuffing. \n
			:param stuffing_hp: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(stuffing_hp)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:STUFfing:HIGH {param}')
