from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtf:
	"""Rtf commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtf", core, parent)

	def get_aus_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:AUSDelay \n
		Snippet: value: float = driver.source.bb.nr5G.tcw.rtf.get_aus_delay() \n
		No command help available \n
			:return: add_user_delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:AUSDelay?')
		return Conversions.str_to_float(response)

	def set_aus_delay(self, add_user_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:AUSDelay \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_aus_delay(add_user_delay = 1.0) \n
		No command help available \n
			:param add_user_delay: No help available
		"""
		param = Conversions.decimal_value_to_str(add_user_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:AUSDelay {param}')

	def get_bb_selector(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:BBSelector \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.rtf.get_bb_selector() \n
		No command help available \n
			:return: bb_selector: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:BBSelector?')
		return Conversions.str_to_int(response)

	def set_bb_selector(self, bb_selector: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:BBSelector \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_bb_selector(bb_selector = 1) \n
		No command help available \n
			:param bb_selector: No help available
		"""
		param = Conversions.decimal_value_to_str(bb_selector)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:BBSelector {param}')

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.FeedbackConnectorAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:CONNector \n
		Snippet: value: enums.FeedbackConnectorAll = driver.source.bb.nr5G.tcw.rtf.get_connector() \n
		No command help available \n
			:return: connector: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnectorAll)

	def set_connector(self, connector: enums.FeedbackConnectorAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:CONNector \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_connector(connector = enums.FeedbackConnectorAll.GLOBal) \n
		No command help available \n
			:param connector: No help available
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.FeedbackConnectorAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:CONNector {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.TcwfEedbackMode:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:MODE \n
		Snippet: value: enums.TcwfEedbackMode = driver.source.bb.nr5G.tcw.rtf.get_mode() \n
		No command help available \n
			:return: rtf_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TcwfEedbackMode)

	def set_mode(self, rtf_mode: enums.TcwfEedbackMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:MODE \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_mode(rtf_mode = enums.TcwfEedbackMode.S3X8) \n
		No command help available \n
			:param rtf_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(rtf_mode, enums.TcwfEedbackMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:MODE {param}')

	# noinspection PyTypeChecker
	def get_ser_rate(self) -> enums.FeedbackRateAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:SERRate \n
		Snippet: value: enums.FeedbackRateAll = driver.source.bb.nr5G.tcw.rtf.get_ser_rate() \n
		No command help available \n
			:return: serial_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:RTF:SERRate?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackRateAll)

	def set_ser_rate(self, serial_rate: enums.FeedbackRateAll) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:RTF:SERRate \n
		Snippet: driver.source.bb.nr5G.tcw.rtf.set_ser_rate(serial_rate = enums.FeedbackRateAll.R115) \n
		No command help available \n
			:param serial_rate: No help available
		"""
		param = Conversions.enum_scalar_to_str(serial_rate, enums.FeedbackRateAll)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:RTF:SERRate {param}')
