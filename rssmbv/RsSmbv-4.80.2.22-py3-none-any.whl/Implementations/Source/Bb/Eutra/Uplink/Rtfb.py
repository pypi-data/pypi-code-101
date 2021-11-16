from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtfb:
	"""Rtfb commands group definition. 16 total commands, 0 Sub-groups, 16 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtfb", core, parent)

	def get_aack(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:AACK \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.rtfb.get_aack() \n
		No command help available \n
			:return: assume_ack: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:AACK?')
		return Conversions.str_to_bool(response)

	def set_aack(self, assume_ack: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:AACK \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_aack(assume_ack = False) \n
		No command help available \n
			:param assume_ack: No help available
		"""
		param = Conversions.bool_to_str(assume_ack)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:AACK {param}')

	# noinspection PyTypeChecker
	def get_ack_definition(self) -> enums.LowHigh:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ACKDefinition \n
		Snippet: value: enums.LowHigh = driver.source.bb.eutra.uplink.rtfb.get_ack_definition() \n
		No command help available \n
			:return: ack_definition: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ACKDefinition?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def set_ack_definition(self, ack_definition: enums.LowHigh) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ACKDefinition \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_ack_definition(ack_definition = enums.LowHigh.HIGH) \n
		No command help available \n
			:param ack_definition: No help available
		"""
		param = Conversions.enum_scalar_to_str(ack_definition, enums.LowHigh)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ACKDefinition {param}')

	def get_adu_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ADUDelay \n
		Snippet: value: float = driver.source.bb.eutra.uplink.rtfb.get_adu_delay() \n
		No command help available \n
			:return: add_user_delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ADUDelay?')
		return Conversions.str_to_float(response)

	def set_adu_delay(self, add_user_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ADUDelay \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_adu_delay(add_user_delay = 1.0) \n
		No command help available \n
			:param add_user_delay: No help available
		"""
		param = Conversions.decimal_value_to_str(add_user_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ADUDelay {param}')

	def get_bb_selector(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BBSelector \n
		Snippet: value: int = driver.source.bb.eutra.uplink.rtfb.get_bb_selector() \n
		No command help available \n
			:return: baseband_select: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BBSelector?')
		return Conversions.str_to_int(response)

	def set_bb_selector(self, baseband_select: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BBSelector \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_bb_selector(baseband_select = 1) \n
		No command help available \n
			:param baseband_select: No help available
		"""
		param = Conversions.decimal_value_to_str(baseband_select)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BBSelector {param}')

	# noinspection PyTypeChecker
	def get_be_insertion(self) -> enums.EutraFeedbackBlerMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BEINsertion \n
		Snippet: value: enums.EutraFeedbackBlerMode = driver.source.bb.eutra.uplink.rtfb.get_be_insertion() \n
		No command help available \n
			:return: block_err_insert: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BEINsertion?')
		return Conversions.str_to_scalar_enum(response, enums.EutraFeedbackBlerMode)

	def set_be_insertion(self, block_err_insert: enums.EutraFeedbackBlerMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BEINsertion \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_be_insertion(block_err_insert = enums.EutraFeedbackBlerMode.APRocesses) \n
		No command help available \n
			:param block_err_insert: No help available
		"""
		param = Conversions.enum_scalar_to_str(block_err_insert, enums.EutraFeedbackBlerMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BEINsertion {param}')

	def get_bit_error_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BERate \n
		Snippet: value: float = driver.source.bb.eutra.uplink.rtfb.get_bit_error_rate() \n
		No command help available \n
			:return: block_err_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BERate?')
		return Conversions.str_to_float(response)

	def set_bit_error_rate(self, block_err_rate: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:BERate \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_bit_error_rate(block_err_rate = 1.0) \n
		No command help available \n
			:param block_err_rate: No help available
		"""
		param = Conversions.decimal_value_to_str(block_err_rate)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:BERate {param}')

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.FeedbackConnector:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:CONNector \n
		Snippet: value: enums.FeedbackConnector = driver.source.bb.eutra.uplink.rtfb.get_connector() \n
		No command help available \n
			:return: connector: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnector)

	def set_connector(self, connector: enums.FeedbackConnector) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:CONNector \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_connector(connector = enums.FeedbackConnector.LEVatt) \n
		No command help available \n
			:param connector: No help available
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.FeedbackConnector)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:CONNector {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.EutraFeedbackDistMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:DMODe \n
		Snippet: value: enums.EutraFeedbackDistMode = driver.source.bb.eutra.uplink.rtfb.get_dmode() \n
		No command help available \n
			:return: distance_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.EutraFeedbackDistMode)

	def set_dmode(self, distance_mode: enums.EutraFeedbackDistMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:DMODe \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_dmode(distance_mode = enums.EutraFeedbackDistMode.DIRect) \n
		No command help available \n
			:param distance_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(distance_mode, enums.EutraFeedbackDistMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:DMODe {param}')

	def get_gen_reports(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:GENReports \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.rtfb.get_gen_reports() \n
		No command help available \n
			:return: gen_debug_reports: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:GENReports?')
		return Conversions.str_to_bool(response)

	def set_gen_reports(self, gen_debug_reports: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:GENReports \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_gen_reports(gen_debug_reports = False) \n
		No command help available \n
			:param gen_debug_reports: No help available
		"""
		param = Conversions.bool_to_str(gen_debug_reports)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:GENReports {param}')

	def get_it_advance(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ITADvance \n
		Snippet: value: int = driver.source.bb.eutra.uplink.rtfb.get_it_advance() \n
		No command help available \n
			:return: init_tim_advance: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ITADvance?')
		return Conversions.str_to_int(response)

	def set_it_advance(self, init_tim_advance: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ITADvance \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_it_advance(init_tim_advance = 1) \n
		No command help available \n
			:param init_tim_advance: No help available
		"""
		param = Conversions.decimal_value_to_str(init_tim_advance)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ITADvance {param}')

	def get_ita_feedback(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ITAFeedback \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.rtfb.get_ita_feedback() \n
		No command help available \n
			:return: ignore_timing_adj: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ITAFeedback?')
		return Conversions.str_to_bool(response)

	def set_ita_feedback(self, ignore_timing_adj: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:ITAFeedback \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_ita_feedback(ignore_timing_adj = False) \n
		No command help available \n
			:param ignore_timing_adj: No help available
		"""
		param = Conversions.bool_to_str(ignore_timing_adj)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:ITAFeedback {param}')

	def get_loffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:LOFFset \n
		Snippet: value: int = driver.source.bb.eutra.uplink.rtfb.get_loffset() \n
		No command help available \n
			:return: logging_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:LOFFset?')
		return Conversions.str_to_int(response)

	def set_loffset(self, logging_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:LOFFset \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_loffset(logging_offset = 1) \n
		No command help available \n
			:param logging_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(logging_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:LOFFset {param}')

	def get_max_trans(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:MAXTrans \n
		Snippet: value: int = driver.source.bb.eutra.uplink.rtfb.get_max_trans() \n
		No command help available \n
			:return: max_transmission: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:MAXTrans?')
		return Conversions.str_to_int(response)

	def set_max_trans(self, max_transmission: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:MAXTrans \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_max_trans(max_transmission = 1) \n
		No command help available \n
			:param max_transmission: No help available
		"""
		param = Conversions.decimal_value_to_str(max_transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:MAXTrans {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.EutraFeedbackMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:MODE \n
		Snippet: value: enums.EutraFeedbackMode = driver.source.bb.eutra.uplink.rtfb.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EutraFeedbackMode)

	def set_mode(self, mode: enums.EutraFeedbackMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:MODE \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_mode(mode = enums.EutraFeedbackMode.BAN) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EutraFeedbackMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:MODE {param}')

	def get_rv_sequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:RVSequence \n
		Snippet: value: str = driver.source.bb.eutra.uplink.rtfb.get_rv_sequence() \n
		No command help available \n
			:return: red_vers_sequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:RVSequence?')
		return trim_str_response(response)

	def set_rv_sequence(self, red_vers_sequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:RVSequence \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_rv_sequence(red_vers_sequence = '1') \n
		No command help available \n
			:param red_vers_sequence: No help available
		"""
		param = Conversions.value_to_quoted_str(red_vers_sequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:RVSequence {param}')

	# noinspection PyTypeChecker
	def get_ser_rte(self) -> enums.EutraSerialRate:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:SERate \n
		Snippet: value: enums.EutraSerialRate = driver.source.bb.eutra.uplink.rtfb.get_ser_rte() \n
		No command help available \n
			:return: serial_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:UL:RTFB:SERate?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSerialRate)

	def set_ser_rte(self, serial_rate: enums.EutraSerialRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:RTFB:SERate \n
		Snippet: driver.source.bb.eutra.uplink.rtfb.set_ser_rte(serial_rate = enums.EutraSerialRate.SR1_6M) \n
		No command help available \n
			:param serial_rate: No help available
		"""
		param = Conversions.enum_scalar_to_str(serial_rate, enums.EutraSerialRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:RTFB:SERate {param}')
