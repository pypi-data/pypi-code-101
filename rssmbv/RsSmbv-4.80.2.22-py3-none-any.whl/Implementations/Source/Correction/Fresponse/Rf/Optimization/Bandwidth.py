from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManualMode:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:OPTimization:BANDwidth:MODE \n
		Snippet: value: enums.AutoManualMode = driver.source.correction.fresponse.rf.optimization.bandwidth.get_mode() \n
		For CORRection:FRESponse:RF:OPTimization:MODEQHIG|QHT, sets how the signal bandwidth is estimated: automatically or
		manually with the command CORRection:FRESponse:RF:OPTimization. \n
			:return: freq_resp_opt_bw_mo: AUTO| MANual
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:OPTimization:BANDwidth:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_mode(self, freq_resp_opt_bw_mo: enums.AutoManualMode) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:OPTimization:BANDwidth:MODE \n
		Snippet: driver.source.correction.fresponse.rf.optimization.bandwidth.set_mode(freq_resp_opt_bw_mo = enums.AutoManualMode.AUTO) \n
		For CORRection:FRESponse:RF:OPTimization:MODEQHIG|QHT, sets how the signal bandwidth is estimated: automatically or
		manually with the command CORRection:FRESponse:RF:OPTimization. \n
			:param freq_resp_opt_bw_mo: AUTO| MANual
		"""
		param = Conversions.enum_scalar_to_str(freq_resp_opt_bw_mo, enums.AutoManualMode)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:OPTimization:BANDwidth:MODE {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:OPTimization:BANDwidth:[VALue] \n
		Snippet: value: int = driver.source.correction.fresponse.rf.optimization.bandwidth.get_value() \n
		Sets the signal compensation bandwidth for CORRection:FRESponse:RF:OPTimization:BANDwidth:MODE MAN. \n
			:return: freq_resp_opt_bw_va: integer Range: depends on installed baseband extension option * e.g. for base unit without extensions max = 120 MHz For more information, see data sheet.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:OPTimization:BANDwidth:VALue?')
		return Conversions.str_to_int(response)

	def set_value(self, freq_resp_opt_bw_va: int) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:OPTimization:BANDwidth:[VALue] \n
		Snippet: driver.source.correction.fresponse.rf.optimization.bandwidth.set_value(freq_resp_opt_bw_va = 1) \n
		Sets the signal compensation bandwidth for CORRection:FRESponse:RF:OPTimization:BANDwidth:MODE MAN. \n
			:param freq_resp_opt_bw_va: integer Range: depends on installed baseband extension option * e.g. for base unit without extensions max = 120 MHz For more information, see data sheet.
		"""
		param = Conversions.decimal_value_to_str(freq_resp_opt_bw_va)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:OPTimization:BANDwidth:VALue {param}')
