from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IsPy:
	"""IsPy commands group definition. 19 total commands, 0 Sub-groups, 19 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isPy", core, parent)

	# noinspection PyTypeChecker
	def get_chbw(self) -> enums.EutraCaChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:CHBW \n
		Snippet: value: enums.EutraCaChannelBandwidth = driver.source.bb.eutra.tcw.isPy.get_chbw() \n
		Queries the channel bandwidth of the interfering signal. \n
			:return: chan_bandwidth: BW20_00| BW10_00| BW5_00| BW3_00| BW1_40| BW15_00
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:CHBW?')
		return Conversions.str_to_scalar_enum(response, enums.EutraCaChannelBandwidth)

	def get_clid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:CLID \n
		Snippet: value: int = driver.source.bb.eutra.tcw.isPy.get_clid() \n
		Sets the Cell ID for the interfering signal. \n
			:return: cell_id: integer Range: 0 to 503
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:CLID?')
		return Conversions.str_to_int(response)

	def set_clid(self, cell_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:CLID \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_clid(cell_id = 1) \n
		Sets the Cell ID for the interfering signal. \n
			:param cell_id: integer Range: 0 to 503
		"""
		param = Conversions.decimal_value_to_str(cell_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:CLID {param}')

	# noinspection PyTypeChecker
	def get_duplex(self) -> enums.EutraDuplexMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:DUPLex \n
		Snippet: value: enums.EutraDuplexMode = driver.source.bb.eutra.tcw.isPy.get_duplex() \n
		Selects whether TDD or FDD duplexing mode is used. \n
			:return: duplex: TDD| FDD
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:DUPLex?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDuplexMode)

	def set_duplex(self, duplex: enums.EutraDuplexMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:DUPLex \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_duplex(duplex = enums.EutraDuplexMode.FDD) \n
		Selects whether TDD or FDD duplexing mode is used. \n
			:param duplex: TDD| FDD
		"""
		param = Conversions.enum_scalar_to_str(duplex, enums.EutraDuplexMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:DUPLex {param}')

	# noinspection PyTypeChecker
	def get_fr_shift(self) -> enums.EutraTcwfReqShift:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:FRSHift \n
		Snippet: value: enums.EutraTcwfReqShift = driver.source.bb.eutra.tcw.isPy.get_fr_shift() \n
		No command help available \n
			:return: frequency_shift: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:FRSHift?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwfReqShift)

	def set_fr_shift(self, frequency_shift: enums.EutraTcwfReqShift) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:FRSHift \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_fr_shift(frequency_shift = enums.EutraTcwfReqShift.FS0) \n
		No command help available \n
			:param frequency_shift: No help available
		"""
		param = Conversions.enum_scalar_to_str(frequency_shift, enums.EutraTcwfReqShift)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:FRSHift {param}')

	# noinspection PyTypeChecker
	def get_if_type(self) -> enums.EutraTcwInterfType:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:IFTYpe \n
		Snippet: value: enums.EutraTcwInterfType = driver.source.bb.eutra.tcw.isPy.get_if_type() \n
			INTRO_CMD_HELP: Selects the type of the interfering signal: \n
			- For Blocking tests, the interfering signal can be an in-band EUTRA/LTE signal (EUTra) or out-of-band CW signal (CW) .
			- For Receiver Intermodulation tests, the first interfering signal can be an EUTRA/LTE signal (EUTra) or narrowband EUTRA signal (NEUTra) . The second interfering signal is always a CW signal (CW) . \n
			:return: interferer_type: NEUTra| EUTra| CW| UTRA
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:IFTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwInterfType)

	def set_if_type(self, interferer_type: enums.EutraTcwInterfType) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:IFTYpe \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_if_type(interferer_type = enums.EutraTcwInterfType.CW) \n
			INTRO_CMD_HELP: Selects the type of the interfering signal: \n
			- For Blocking tests, the interfering signal can be an in-band EUTRA/LTE signal (EUTra) or out-of-band CW signal (CW) .
			- For Receiver Intermodulation tests, the first interfering signal can be an EUTRA/LTE signal (EUTra) or narrowband EUTRA signal (NEUTra) . The second interfering signal is always a CW signal (CW) . \n
			:param interferer_type: NEUTra| EUTra| CW| UTRA
		"""
		param = Conversions.enum_scalar_to_str(interferer_type, enums.EutraTcwInterfType)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:IFTYpe {param}')

	def get_nrblock(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:NRBLock \n
		Snippet: value: int = driver.source.bb.eutra.tcw.isPy.get_nrblock() \n
		Queries the number of RBs used by the LTE interfering signal. \n
			:return: num_res_block: integer Range: 3 to 25
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:NRBLock?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_nta_offset(self) -> enums.EutraTcwsIgAdvNtaOffs:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:NTAOffset \n
		Snippet: value: enums.EutraTcwsIgAdvNtaOffs = driver.source.bb.eutra.tcw.isPy.get_nta_offset() \n
		Sets the parameter NTAoffset. \n
			:return: sig_adv_nta_offset: NTA624| NTA0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:NTAOffset?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwsIgAdvNtaOffs)

	def set_nta_offset(self, sig_adv_nta_offset: enums.EutraTcwsIgAdvNtaOffs) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:NTAOffset \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_nta_offset(sig_adv_nta_offset = enums.EutraTcwsIgAdvNtaOffs.NTA0) \n
		Sets the parameter NTAoffset. \n
			:param sig_adv_nta_offset: NTA624| NTA0
		"""
		param = Conversions.enum_scalar_to_str(sig_adv_nta_offset, enums.EutraTcwsIgAdvNtaOffs)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:NTAOffset {param}')

	# noinspection PyTypeChecker
	def get_oc_edge(self) -> enums.EutraTcwoFfsChanEdge:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:OCEDge \n
		Snippet: value: enums.EutraTcwoFfsChanEdge = driver.source.bb.eutra.tcw.isPy.get_oc_edge() \n
		Defines the offset of the interfering signal center frequency relative to edge of the wanted channel bandwidth. \n
			:return: offset_channel_edge: OCE12_5| OCE7_5| OCE2_5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:OCEDge?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwoFfsChanEdge)

	def set_oc_edge(self, offset_channel_edge: enums.EutraTcwoFfsChanEdge) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:OCEDge \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_oc_edge(offset_channel_edge = enums.EutraTcwoFfsChanEdge.OCE12_5) \n
		Defines the offset of the interfering signal center frequency relative to edge of the wanted channel bandwidth. \n
			:param offset_channel_edge: OCE12_5| OCE7_5| OCE2_5
		"""
		param = Conversions.enum_scalar_to_str(offset_channel_edge, enums.EutraTcwoFfsChanEdge)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:OCEDge {param}')

	def get_ort_cover(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:ORTCover \n
		Snippet: value: int = driver.source.bb.eutra.tcw.isPy.get_ort_cover() \n
		No command help available \n
			:return: ortho_cover: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:ORTCover?')
		return Conversions.str_to_int(response)

	def get_ovrb(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:OVRB \n
		Snippet: value: int = driver.source.bb.eutra.tcw.isPy.get_ovrb() \n
		No command help available \n
			:return: offset_vrb: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:OVRB?')
		return Conversions.str_to_int(response)

	def get_plevel(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:PLEVel \n
		Snippet: value: str = driver.source.bb.eutra.tcw.isPy.get_plevel() \n
		Queries the power level of the interfering signal. \n
			:return: power_level: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:PLEVel?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_pr_condition(self) -> enums.EutraTcwPropagCond:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:PRCOndition \n
		Snippet: value: enums.EutraTcwPropagCond = driver.source.bb.eutra.tcw.isPy.get_pr_condition() \n
		No command help available \n
			:return: propagation_condition: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:PRCOndition?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwPropagCond)

	def get_rbc_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:RBCFrequency \n
		Snippet: value: int = driver.source.bb.eutra.tcw.isPy.get_rbc_frequency() \n
		No command help available \n
			:return: rblock_cent_freq: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:RBCFrequency?')
		return Conversions.str_to_int(response)

	def get_rf_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:RFFRequency \n
		Snippet: value: int = driver.source.bb.eutra.tcw.isPy.get_rf_frequency() \n
		Queries the center frequency of the interfering signal. \n
			:return: rf_frequency: integer Range: 100E3 to 6E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:RFFRequency?')
		return Conversions.str_to_int(response)

	def set_rf_frequency(self, rf_frequency: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:RFFRequency \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_rf_frequency(rf_frequency = 1) \n
		Queries the center frequency of the interfering signal. \n
			:param rf_frequency: integer Range: 100E3 to 6E9
		"""
		param = Conversions.decimal_value_to_str(rf_frequency)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:RFFRequency {param}')

	def get_tdd_config(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:TDDConfig \n
		Snippet: value: int = driver.source.bb.eutra.tcw.isPy.get_tdd_config() \n
		For TDD mode, selects the UL/DL Configuration number. \n
			:return: tdd_config: integer Range: 0 to 6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:TDDConfig?')
		return Conversions.str_to_int(response)

	def set_tdd_config(self, tdd_config: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:TDDConfig \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_tdd_config(tdd_config = 1) \n
		For TDD mode, selects the UL/DL Configuration number. \n
			:param tdd_config: integer Range: 0 to 6
		"""
		param = Conversions.decimal_value_to_str(tdd_config)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:TDDConfig {param}')

	# noinspection PyTypeChecker
	def get_tm_codes(self) -> enums.UtraTcwtMcodes:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:TMCodes \n
		Snippet: value: enums.UtraTcwtMcodes = driver.source.bb.eutra.tcw.isPy.get_tm_codes() \n
		No command help available \n
			:return: test_model_1_codes: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:TMCodes?')
		return Conversions.str_to_scalar_enum(response, enums.UtraTcwtMcodes)

	def set_tm_codes(self, test_model_1_codes: enums.UtraTcwtMcodes) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:TMCodes \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_tm_codes(test_model_1_codes = enums.UtraTcwtMcodes.COD16) \n
		No command help available \n
			:param test_model_1_codes: No help available
		"""
		param = Conversions.enum_scalar_to_str(test_model_1_codes, enums.UtraTcwtMcodes)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:TMCodes {param}')

	# noinspection PyTypeChecker
	def get_tmodel(self) -> enums.TestModel:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:TMODel \n
		Snippet: value: enums.TestModel = driver.source.bb.eutra.tcw.isPy.get_tmodel() \n
		Queries the test model. The interfering signal is generated according to E-TM1.1 test model. \n
			:return: test_model: TM1_1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:TMODel?')
		return Conversions.str_to_scalar_enum(response, enums.TestModel)

	# noinspection PyTypeChecker
	def get_trequire(self) -> enums.TestRequire:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:TREQuire \n
		Snippet: value: enums.TestRequire = driver.source.bb.eutra.tcw.isPy.get_trequire() \n
		No command help available \n
			:return: test_require: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:TREQuire?')
		return Conversions.str_to_scalar_enum(response, enums.TestRequire)

	def set_trequire(self, test_require: enums.TestRequire) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:TREQuire \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_trequire(test_require = enums.TestRequire.BLPE) \n
		No command help available \n
			:param test_require: No help available
		"""
		param = Conversions.enum_scalar_to_str(test_require, enums.TestRequire)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:TREQuire {param}')

	def get_ue_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:UEID \n
		Snippet: value: int = driver.source.bb.eutra.tcw.isPy.get_ue_id() \n
		Sets the UE ID/n_RNTI for the interfering signal. \n
			:return: ue_idn_rnti: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS:UEID?')
		return Conversions.str_to_int(response)

	def set_ue_id(self, ue_idn_rnti: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS:UEID \n
		Snippet: driver.source.bb.eutra.tcw.isPy.set_ue_id(ue_idn_rnti = 1) \n
		Sets the UE ID/n_RNTI for the interfering signal. \n
			:param ue_idn_rnti: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(ue_idn_rnti)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TCW:IS:UEID {param}')
