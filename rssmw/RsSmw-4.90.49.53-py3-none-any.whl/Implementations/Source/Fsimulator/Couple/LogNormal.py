from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LogNormal:
	"""LogNormal commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logNormal", core, parent)

	def get_cstd(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:COUPle:LOGNormal:CSTD \n
		Snippet: value: bool = driver.source.fsimulator.couple.logNormal.get_cstd() \n
		(available in 'System Configuration > Mode > Standard') Couples the lognormal fading setting. \n
			:return: cstd: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:COUPle:LOGNormal:CSTD?')
		return Conversions.str_to_bool(response)

	def set_cstd(self, cstd: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:COUPle:LOGNormal:CSTD \n
		Snippet: driver.source.fsimulator.couple.logNormal.set_cstd(cstd = False) \n
		(available in 'System Configuration > Mode > Standard') Couples the lognormal fading setting. \n
			:param cstd: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(cstd)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:COUPle:LOGNormal:CSTD {param}')

	def get_lconstant(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:COUPle:LOGNormal:LCONstant \n
		Snippet: value: bool = driver.source.fsimulator.couple.logNormal.get_lconstant() \n
		(available in 'System Configuration > Mode > Standard') Couples the lognormal fading setting. \n
			:return: lconstant: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:COUPle:LOGNormal:LCONstant?')
		return Conversions.str_to_bool(response)

	def set_lconstant(self, lconstant: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:COUPle:LOGNormal:LCONstant \n
		Snippet: driver.source.fsimulator.couple.logNormal.set_lconstant(lconstant = False) \n
		(available in 'System Configuration > Mode > Standard') Couples the lognormal fading setting. \n
			:param lconstant: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(lconstant)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:COUPle:LOGNormal:LCONstant {param}')
