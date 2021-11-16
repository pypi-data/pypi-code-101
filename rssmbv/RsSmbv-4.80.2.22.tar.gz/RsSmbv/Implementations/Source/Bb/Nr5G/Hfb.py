from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hfb:
	"""Hfb commands group definition. 11 total commands, 0 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hfb", core, parent)

	def get_adj_cmd(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:ADJCmd \n
		Snippet: value: int = driver.source.bb.nr5G.hfb.get_adj_cmd() \n
		No command help available \n
			:return: init_timing_adj_cm: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:ADJCmd?')
		return Conversions.str_to_int(response)

	def set_adj_cmd(self, init_timing_adj_cm: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:ADJCmd \n
		Snippet: driver.source.bb.nr5G.hfb.set_adj_cmd(init_timing_adj_cm = 1) \n
		No command help available \n
			:param init_timing_adj_cm: No help available
		"""
		param = Conversions.decimal_value_to_str(init_timing_adj_cm)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:ADJCmd {param}')

	def get_baseband(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:BASeband \n
		Snippet: value: int = driver.source.bb.nr5G.hfb.get_baseband() \n
		No command help available \n
			:return: fb_baseband: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:BASeband?')
		return Conversions.str_to_int(response)

	def set_baseband(self, fb_baseband: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:BASeband \n
		Snippet: driver.source.bb.nr5G.hfb.set_baseband(fb_baseband = 1) \n
		No command help available \n
			:param fb_baseband: No help available
		"""
		param = Conversions.decimal_value_to_str(fb_baseband)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:BASeband {param}')

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.FeedbackConnectorAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:CONNector \n
		Snippet: value: enums.FeedbackConnectorAll = driver.source.bb.nr5G.hfb.get_connector() \n
		No command help available \n
			:return: fb_connector: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnectorAll)

	def set_connector(self, fb_connector: enums.FeedbackConnectorAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:CONNector \n
		Snippet: driver.source.bb.nr5G.hfb.set_connector(fb_connector = enums.FeedbackConnectorAll.GLOBal) \n
		No command help available \n
			:param fb_connector: No help available
		"""
		param = Conversions.enum_scalar_to_str(fb_connector, enums.FeedbackConnectorAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:CONNector {param}')

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:DELay \n
		Snippet: value: float = driver.source.bb.nr5G.hfb.get_delay() \n
		No command help available \n
			:return: fb_user_delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, fb_user_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:DELay \n
		Snippet: driver.source.bb.nr5G.hfb.set_delay(fb_user_delay = 1.0) \n
		No command help available \n
			:param fb_user_delay: No help available
		"""
		param = Conversions.decimal_value_to_str(fb_user_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:DELay {param}')

	def get_hpn_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:HPNMode \n
		Snippet: value: bool = driver.source.bb.nr5G.hfb.get_hpn_mode() \n
		No command help available \n
			:return: hpn_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:HPNMode?')
		return Conversions.str_to_bool(response)

	def set_hpn_mode(self, hpn_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:HPNMode \n
		Snippet: driver.source.bb.nr5G.hfb.set_hpn_mode(hpn_mode = False) \n
		No command help available \n
			:param hpn_mode: No help available
		"""
		param = Conversions.bool_to_str(hpn_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:HPNMode {param}')

	def get_log_path(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:LOGPath \n
		Snippet: value: str = driver.source.bb.nr5G.hfb.get_log_path() \n
		No command help available \n
			:return: log_gen_output_path: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:LOGPath?')
		return trim_str_response(response)

	def set_log_path(self, log_gen_output_path: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:LOGPath \n
		Snippet: driver.source.bb.nr5G.hfb.set_log_path(log_gen_output_path = '1') \n
		No command help available \n
			:param log_gen_output_path: No help available
		"""
		param = Conversions.value_to_quoted_str(log_gen_output_path)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:LOGPath {param}')

	def get_log_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:LOGState \n
		Snippet: value: bool = driver.source.bb.nr5G.hfb.get_log_state() \n
		No command help available \n
			:return: log_gen_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:LOGState?')
		return Conversions.str_to_bool(response)

	def set_log_state(self, log_gen_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:LOGState \n
		Snippet: driver.source.bb.nr5G.hfb.set_log_state(log_gen_state = False) \n
		No command help available \n
			:param log_gen_state: No help available
		"""
		param = Conversions.bool_to_str(log_gen_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:LOGState {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FeedbackModeAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:MODE \n
		Snippet: value: enums.FeedbackModeAll = driver.source.bb.nr5G.hfb.get_mode() \n
		No command help available \n
			:return: fb_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackModeAll)

	def set_mode(self, fb_mode: enums.FeedbackModeAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:MODE \n
		Snippet: driver.source.bb.nr5G.hfb.set_mode(fb_mode = enums.FeedbackModeAll.OFF) \n
		No command help available \n
			:param fb_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(fb_mode, enums.FeedbackModeAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:MODE {param}')

	def get_pdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:PDELay \n
		Snippet: value: float = driver.source.bb.nr5G.hfb.get_pdelay() \n
		No command help available \n
			:return: processing_delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:PDELay?')
		return Conversions.str_to_float(response)

	def set_pdelay(self, processing_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:PDELay \n
		Snippet: driver.source.bb.nr5G.hfb.set_pdelay(processing_delay = 1.0) \n
		No command help available \n
			:param processing_delay: No help available
		"""
		param = Conversions.decimal_value_to_str(processing_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:PDELay {param}')

	# noinspection PyTypeChecker
	def get_symbol_rate(self) -> enums.FeedbackRateAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:SRATe \n
		Snippet: value: enums.FeedbackRateAll = driver.source.bb.nr5G.hfb.get_symbol_rate() \n
		No command help available \n
			:return: fb_serial_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:SRATe?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackRateAll)

	def set_symbol_rate(self, fb_serial_rate: enums.FeedbackRateAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:SRATe \n
		Snippet: driver.source.bb.nr5G.hfb.set_symbol_rate(fb_serial_rate = enums.FeedbackRateAll.R115) \n
		No command help available \n
			:param fb_serial_rate: No help available
		"""
		param = Conversions.enum_scalar_to_str(fb_serial_rate, enums.FeedbackRateAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:SRATe {param}')

	def get_ta_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:TAMode \n
		Snippet: value: bool = driver.source.bb.nr5G.hfb.get_ta_mode() \n
		No command help available \n
			:return: ta_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:HFB:TAMode?')
		return Conversions.str_to_bool(response)

	def set_ta_mode(self, ta_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:HFB:TAMode \n
		Snippet: driver.source.bb.nr5G.hfb.set_ta_mode(ta_mode = False) \n
		No command help available \n
			:param ta_mode: No help available
		"""
		param = Conversions.bool_to_str(ta_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:HFB:TAMode {param}')
