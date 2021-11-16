from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.Utilities import trim_str_response
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ws:
	"""Ws commands group definition. 27 total commands, 2 Sub-groups, 25 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ws", core, parent)

	@property
	def cqiPattern(self):
		"""cqiPattern commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqiPattern'):
			from .CqiPattern import CqiPattern
			self._cqiPattern = CqiPattern(self._core, self._cmd_group)
		return self._cqiPattern

	@property
	def ortCover(self):
		"""ortCover commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ortCover'):
			from .OrtCover import OrtCover
			self._ortCover = OrtCover(self._core, self._cmd_group)
		return self._ortCover

	def get_ac_pucch(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:ACPucch \n
		Snippet: value: bool = driver.source.bb.eutra.tcw.ws.get_ac_pucch() \n
		No command help available \n
			:return: add_config_pucch: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:ACPucch?')
		return Conversions.str_to_bool(response)

	def set_ac_pucch(self, add_config_pucch: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:ACPucch \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_ac_pucch(add_config_pucch = False) \n
		No command help available \n
			:param add_config_pucch: No help available
		"""
		param = Conversions.bool_to_str(add_config_pucch)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:ACPucch {param}')

	# noinspection PyTypeChecker
	def get_an_bits(self) -> enums.UtraTcwaCkNackBits:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:ANBits \n
		Snippet: value: enums.UtraTcwaCkNackBits = driver.source.bb.eutra.tcw.ws.get_an_bits() \n
		No command help available \n
			:return: ack_nack_bits: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:ANBits?')
		return Conversions.str_to_scalar_enum(response, enums.UtraTcwaCkNackBits)

	def set_an_bits(self, ack_nack_bits: enums.UtraTcwaCkNackBits) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:ANBits \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_an_bits(ack_nack_bits = enums.UtraTcwaCkNackBits.ANB16) \n
		No command help available \n
			:param ack_nack_bits: No help available
		"""
		param = Conversions.enum_scalar_to_str(ack_nack_bits, enums.UtraTcwaCkNackBits)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:ANBits {param}')

	# noinspection PyTypeChecker
	class AnPatternStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Ack_Nack_Pattern: List[str]: No parameter help available
			- Bitcount: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Ack_Nack_Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ack_Nack_Pattern: List[str] = None
			self.Bitcount: int = None

	def get_an_pattern(self) -> AnPatternStruct:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:ANPattern \n
		Snippet: value: AnPatternStruct = driver.source.bb.eutra.tcw.ws.get_an_pattern() \n
		No command help available \n
			:return: structure: for return value, see the help for AnPatternStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:BB:EUTRa:TCW:WS:ANPattern?', self.__class__.AnPatternStruct())

	# noinspection PyTypeChecker
	def get_bformat(self) -> enums.EutraTcwBurstFormat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:BFORmat \n
		Snippet: value: enums.EutraTcwBurstFormat = driver.source.bb.eutra.tcw.ws.get_bformat() \n
		No command help available \n
			:return: burst_format: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:BFORmat?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwBurstFormat)

	def set_bformat(self, burst_format: enums.EutraTcwBurstFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:BFORmat \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_bformat(burst_format = enums.EutraTcwBurstFormat.BF0) \n
		No command help available \n
			:param burst_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(burst_format, enums.EutraTcwBurstFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:BFORmat {param}')

	# noinspection PyTypeChecker
	def get_chbw(self) -> enums.EutraCaChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:CHBW \n
		Snippet: value: enums.EutraCaChannelBandwidth = driver.source.bb.eutra.tcw.ws.get_chbw() \n
		Selects the channel bandwidth. \n
			:return: chan_bandwidth: BW20_00| BW10_00| BW5_00| BW3_00| BW1_40| BW15_00
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:CHBW?')
		return Conversions.str_to_scalar_enum(response, enums.EutraCaChannelBandwidth)

	def set_chbw(self, chan_bandwidth: enums.EutraCaChannelBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:CHBW \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_chbw(chan_bandwidth = enums.EutraCaChannelBandwidth.BW1_40) \n
		Selects the channel bandwidth. \n
			:param chan_bandwidth: BW20_00| BW10_00| BW5_00| BW3_00| BW1_40| BW15_00
		"""
		param = Conversions.enum_scalar_to_str(chan_bandwidth, enums.EutraCaChannelBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:CHBW {param}')

	def get_clid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:CLID \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.get_clid() \n
		Sets the Cell ID. \n
			:return: cell_id: integer Range: 0 to 503
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:CLID?')
		return Conversions.str_to_int(response)

	def set_clid(self, cell_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:CLID \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_clid(cell_id = 1) \n
		Sets the Cell ID. \n
			:param cell_id: integer Range: 0 to 503
		"""
		param = Conversions.decimal_value_to_str(cell_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:CLID {param}')

	# noinspection PyTypeChecker
	def get_cyc_prefix(self) -> enums.EuTraDuration:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:CYCPrefix \n
		Snippet: value: enums.EuTraDuration = driver.source.bb.eutra.tcw.ws.get_cyc_prefix() \n
		Selects normal or extended cyclic prefix. \n
			:return: cyclic_prefix: EXTended| NORMal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:CYCPrefix?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraDuration)

	def set_cyc_prefix(self, cyclic_prefix: enums.EuTraDuration) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:CYCPrefix \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_cyc_prefix(cyclic_prefix = enums.EuTraDuration.EXTended) \n
		Selects normal or extended cyclic prefix. \n
			:param cyclic_prefix: EXTended| NORMal
		"""
		param = Conversions.enum_scalar_to_str(cyclic_prefix, enums.EuTraDuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:CYCPrefix {param}')

	# noinspection PyTypeChecker
	def get_duplex(self) -> enums.EutraDuplexMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:DUPLex \n
		Snippet: value: enums.EutraDuplexMode = driver.source.bb.eutra.tcw.ws.get_duplex() \n
		Selects whether TDD or FDD duplexing mode is used. \n
			:return: duplex: TDD| FDD
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:DUPLex?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDuplexMode)

	def set_duplex(self, duplex: enums.EutraDuplexMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:DUPLex \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_duplex(duplex = enums.EutraDuplexMode.FDD) \n
		Selects whether TDD or FDD duplexing mode is used. \n
			:param duplex: TDD| FDD
		"""
		param = Conversions.enum_scalar_to_str(duplex, enums.EutraDuplexMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:DUPLex {param}')

	# noinspection PyTypeChecker
	def get_fm_throughput(self) -> enums.EutraTcwfRactMaxThroughput:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:FMTHroughput \n
		Snippet: value: enums.EutraTcwfRactMaxThroughput = driver.source.bb.eutra.tcw.ws.get_fm_throughput() \n
		No command help available \n
			:return: fract_max_through: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:FMTHroughput?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwfRactMaxThroughput)

	def set_fm_throughput(self, fract_max_through: enums.EutraTcwfRactMaxThroughput) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:FMTHroughput \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_fm_throughput(fract_max_through = enums.EutraTcwfRactMaxThroughput.FMT30) \n
		No command help available \n
			:param fract_max_through: No help available
		"""
		param = Conversions.enum_scalar_to_str(fract_max_through, enums.EutraTcwfRactMaxThroughput)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:FMTHroughput {param}')

	# noinspection PyTypeChecker
	def get_frc(self) -> enums.EutraUlFrc:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:FRC \n
		Snippet: value: enums.EutraUlFrc = driver.source.bb.eutra.tcw.ws.get_frc() \n
		Queries the fixed reference channel used. \n
			:return: frc: A11| A12| A13| A14| A15| A21| A22| A23| A31| A32| A33| A34| A35| A36| A37| A41| A42| A43| A44| A45| A46| A47| A48| A51| A52| A53| A54| A55| A56| A57| A71| A72| A73| A74| A75| A76| A81| A82| A83| A84| A85| A86| UE11| UE12| UE21| UE22| UE3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:FRC?')
		return Conversions.str_to_scalar_enum(response, enums.EutraUlFrc)

	def set_frc(self, frc: enums.EutraUlFrc) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:FRC \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_frc(frc = enums.EutraUlFrc.A11) \n
		Queries the fixed reference channel used. \n
			:param frc: A11| A12| A13| A14| A15| A21| A22| A23| A31| A32| A33| A34| A35| A36| A37| A41| A42| A43| A44| A45| A46| A47| A48| A51| A52| A53| A54| A55| A56| A57| A71| A72| A73| A74| A75| A76| A81| A82| A83| A84| A85| A86| UE11| UE12| UE21| UE22| UE3
		"""
		param = Conversions.enum_scalar_to_str(frc, enums.EutraUlFrc)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:FRC {param}')

	# noinspection PyTypeChecker
	def get_fr_offset(self) -> enums.EutraTcwfReqOffset:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:FROFfset \n
		Snippet: value: enums.EutraTcwfReqOffset = driver.source.bb.eutra.tcw.ws.get_fr_offset() \n
		No command help available \n
			:return: freq_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:FROFfset?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwfReqOffset)

	def set_fr_offset(self, freq_offset: enums.EutraTcwfReqOffset) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:FROFfset \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_fr_offset(freq_offset = enums.EutraTcwfReqOffset.FO_0) \n
		No command help available \n
			:param freq_offset: No help available
		"""
		param = Conversions.enum_scalar_to_str(freq_offset, enums.EutraTcwfReqOffset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:FROFfset {param}')

	def get_hs_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:HSMode \n
		Snippet: value: bool = driver.source.bb.eutra.tcw.ws.get_hs_mode() \n
		No command help available \n
			:return: high_speed_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:HSMode?')
		return Conversions.str_to_bool(response)

	def set_hs_mode(self, high_speed_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:HSMode \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_hs_mode(high_speed_mode = False) \n
		No command help available \n
			:param high_speed_mode: No help available
		"""
		param = Conversions.bool_to_str(high_speed_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:HSMode {param}')

	# noinspection PyTypeChecker
	def get_nta_offset(self) -> enums.EutraTcwsIgAdvNtaOffs:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:NTAOffset \n
		Snippet: value: enums.EutraTcwsIgAdvNtaOffs = driver.source.bb.eutra.tcw.ws.get_nta_offset() \n
		Sets the parameter NTAoffset. \n
			:return: sig_adv_nta_offset: NTA624| NTA0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:NTAOffset?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwsIgAdvNtaOffs)

	def set_nta_offset(self, sig_adv_nta_offset: enums.EutraTcwsIgAdvNtaOffs) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:NTAOffset \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_nta_offset(sig_adv_nta_offset = enums.EutraTcwsIgAdvNtaOffs.NTA0) \n
		Sets the parameter NTAoffset. \n
			:param sig_adv_nta_offset: NTA624| NTA0
		"""
		param = Conversions.enum_scalar_to_str(sig_adv_nta_offset, enums.EutraTcwsIgAdvNtaOffs)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:NTAOffset {param}')

	def get_oup_level(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:OUPLevel \n
		Snippet: value: float = driver.source.bb.eutra.tcw.ws.get_oup_level() \n
		The settings of the selected test case become active only after selecting 'Apply Settings'. \n
			:return: out_power_level: float Range: -115 to 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:OUPLevel?')
		return Conversions.str_to_float(response)

	def set_oup_level(self, out_power_level: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:OUPLevel \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_oup_level(out_power_level = 1.0) \n
		The settings of the selected test case become active only after selecting 'Apply Settings'. \n
			:param out_power_level: float Range: -115 to 0
		"""
		param = Conversions.decimal_value_to_str(out_power_level)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:OUPLevel {param}')

	def get_ovrb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:OVRB \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.get_ovrb() \n
		Sets the number of RB the allocated RB(s) are shifted with. \n
			:return: offset_vrb: integer Range: 0 to 75
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:OVRB?')
		return Conversions.str_to_int(response)

	def set_ovrb(self, offset_vrb: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:OVRB \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_ovrb(offset_vrb = 1) \n
		Sets the number of RB the allocated RB(s) are shifted with. \n
			:param offset_vrb: integer Range: 0 to 75
		"""
		param = Conversions.decimal_value_to_str(offset_vrb)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:OVRB {param}')

	def get_plevel(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:PLEVel \n
		Snippet: value: str = driver.source.bb.eutra.tcw.ws.get_plevel() \n
		Queries the Power Level. \n
			:return: power_level: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:PLEVel?')
		return trim_str_response(response)

	def get_plpc(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:PLPC \n
		Snippet: value: str = driver.source.bb.eutra.tcw.ws.get_plpc() \n
		No command help available \n
			:return: power_level_pucch: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:PLPC?')
		return trim_str_response(response)

	def get_plps(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:PLPS \n
		Snippet: value: str = driver.source.bb.eutra.tcw.ws.get_plps() \n
		No command help available \n
			:return: power_level_pusch: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:PLPS?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_pro_condition(self) -> enums.EutraTcwPropagCond:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:PROCondition \n
		Snippet: value: enums.EutraTcwPropagCond = driver.source.bb.eutra.tcw.ws.get_pro_condition() \n
		No command help available \n
			:return: propagation_cond: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:PROCondition?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwPropagCond)

	def set_pro_condition(self, propagation_cond: enums.EutraTcwPropagCond) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:PROCondition \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_pro_condition(propagation_cond = enums.EutraTcwPropagCond.AWGNonly) \n
		No command help available \n
			:param propagation_cond: No help available
		"""
		param = Conversions.enum_scalar_to_str(propagation_cond, enums.EutraTcwPropagCond)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:PROCondition {param}')

	def get_rf_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:RFFRequency \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.get_rf_frequency() \n
		Sets the RF frequency of the wanted signal. \n
			:return: rf_frequency: integer Range: 100E3 to 6E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:RFFRequency?')
		return Conversions.str_to_int(response)

	def set_rf_frequency(self, rf_frequency: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:RFFRequency \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_rf_frequency(rf_frequency = 1) \n
		Sets the RF frequency of the wanted signal. \n
			:param rf_frequency: integer Range: 100E3 to 6E9
		"""
		param = Conversions.decimal_value_to_str(rf_frequency)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:RFFRequency {param}')

	def get_sps_frame(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:SPSFrame \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.get_sps_frame() \n
		No command help available \n
			:return: spec_subframe: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:SPSFrame?')
		return Conversions.str_to_int(response)

	def set_sps_frame(self, spec_subframe: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:SPSFrame \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_sps_frame(spec_subframe = 1) \n
		No command help available \n
			:param spec_subframe: No help available
		"""
		param = Conversions.decimal_value_to_str(spec_subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:SPSFrame {param}')

	def get_tdd_config(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:TDDConfig \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.get_tdd_config() \n
		For TDD mode, selects the UL/DL Configuration number. \n
			:return: tdd_config: integer Range: 0 to 6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:TDDConfig?')
		return Conversions.str_to_int(response)

	def set_tdd_config(self, tdd_config: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:TDDConfig \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_tdd_config(tdd_config = 1) \n
		For TDD mode, selects the UL/DL Configuration number. \n
			:param tdd_config: integer Range: 0 to 6
		"""
		param = Conversions.decimal_value_to_str(tdd_config)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:TDDConfig {param}')

	def get_tio_base(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:TIOBase \n
		Snippet: value: float = driver.source.bb.eutra.tcw.ws.get_tio_base() \n
		No command help available \n
			:return: timing_offset_base: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:TIOBase?')
		return Conversions.str_to_float(response)

	def get_ue_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:UEID \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.get_ue_id() \n
		Sets the UE ID/n_RNTI. \n
			:return: ue_idn_rnti: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:UEID?')
		return Conversions.str_to_int(response)

	def set_ue_id(self, ue_idn_rnti: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:UEID \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_ue_id(ue_idn_rnti = 1) \n
		Sets the UE ID/n_RNTI. \n
			:param ue_idn_rnti: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(ue_idn_rnti)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:UEID {param}')

	def get_vdr_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:VDRFrequency \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.get_vdr_frequency() \n
		No command help available \n
			:return: virt_dl_rf: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:WS:VDRFrequency?')
		return Conversions.str_to_int(response)

	def set_vdr_frequency(self, virt_dl_rf: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:VDRFrequency \n
		Snippet: driver.source.bb.eutra.tcw.ws.set_vdr_frequency(virt_dl_rf = 1) \n
		No command help available \n
			:param virt_dl_rf: No help available
		"""
		param = Conversions.decimal_value_to_str(virt_dl_rf)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:VDRFrequency {param}')

	def clone(self) -> 'Ws':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ws(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
