from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Powc:
	"""Powc commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powc", core, parent)

	# noinspection PyTypeChecker
	def get_lev_reference(self) -> enums.EutraPowcLevRef:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:POWC:LEVReference \n
		Snippet: value: enums.EutraPowcLevRef = driver.source.bb.eutra.powc.get_lev_reference() \n
		Defines the reference for the 'Level' display in the status bar. \n
			:return: level_reference: FRMS| DRMS| UEBurst | URMS | NPBCH FRMS The displayed RMS and PEP are measured during the whole frame. All frames are considered, not only the first one. DRMS The displayed RMS and PEP are measured during the DL part of the frame (all DL subframes and the DwPTS) . All frames are considered, not only the first one. URMS The displayed RMS and PEP are measured during the UL part of the frame (all UL subframes and the UpPTS) . All frames are considered, not only the first one. UEBurst The displayed RMS and PEP are measured during a single subframe (or slot) of a certain UE. NPBCH In NB-IoT standalone operation, the displayed RMS and PEP are measured during the NPBCH symbols 3, 9 and 11.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:POWC:LEVReference?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPowcLevRef)

	def set_lev_reference(self, level_reference: enums.EutraPowcLevRef) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:POWC:LEVReference \n
		Snippet: driver.source.bb.eutra.powc.set_lev_reference(level_reference = enums.EutraPowcLevRef.DRMS) \n
		Defines the reference for the 'Level' display in the status bar. \n
			:param level_reference: FRMS| DRMS| UEBurst | URMS | NPBCH FRMS The displayed RMS and PEP are measured during the whole frame. All frames are considered, not only the first one. DRMS The displayed RMS and PEP are measured during the DL part of the frame (all DL subframes and the DwPTS) . All frames are considered, not only the first one. URMS The displayed RMS and PEP are measured during the UL part of the frame (all UL subframes and the UpPTS) . All frames are considered, not only the first one. UEBurst The displayed RMS and PEP are measured during a single subframe (or slot) of a certain UE. NPBCH In NB-IoT standalone operation, the displayed RMS and PEP are measured during the NPBCH symbols 3, 9 and 11.
		"""
		param = Conversions.enum_scalar_to_str(level_reference, enums.EutraPowcLevRef)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:POWC:LEVReference {param}')

	def get_ort_level(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:POWC:ORTLevel \n
		Snippet: value: float = driver.source.bb.eutra.powc.get_ort_level() \n
		Sets the power offset of the baseband relative to the RMS level displayed in the instrument's global Level display in the
		header of the instrument. \n
			:return: offset_relative_level: float Range: -20 to 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:POWC:ORTLevel?')
		return Conversions.str_to_float(response)

	def set_ort_level(self, offset_relative_level: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:POWC:ORTLevel \n
		Snippet: driver.source.bb.eutra.powc.set_ort_level(offset_relative_level = 1.0) \n
		Sets the power offset of the baseband relative to the RMS level displayed in the instrument's global Level display in the
		header of the instrument. \n
			:param offset_relative_level: float Range: -20 to 0
		"""
		param = Conversions.decimal_value_to_str(offset_relative_level)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:POWC:ORTLevel {param}')

	# noinspection PyTypeChecker
	def get_ref_channel(self) -> enums.EutraPowcRefChan:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:POWC:REFChannel \n
		Snippet: value: enums.EutraPowcRefChan = driver.source.bb.eutra.powc.get_ref_channel() \n
		If BB:EUTRa:POWC:LEVReferenceUEBurst, queries the channel type to that the measured RMS and PEP are referring. \n
			:return: ref_channel: NF| PUSCH| PUCCH| PRACH| SRS| PUCPUS | SL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:POWC:REFChannel?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPowcRefChan)

	def set_ref_channel(self, ref_channel: enums.EutraPowcRefChan) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:POWC:REFChannel \n
		Snippet: driver.source.bb.eutra.powc.set_ref_channel(ref_channel = enums.EutraPowcRefChan.NF) \n
		If BB:EUTRa:POWC:LEVReferenceUEBurst, queries the channel type to that the measured RMS and PEP are referring. \n
			:param ref_channel: NF| PUSCH| PUCCH| PRACH| SRS| PUCPUS | SL
		"""
		param = Conversions.enum_scalar_to_str(ref_channel, enums.EutraPowcRefChan)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:POWC:REFChannel {param}')

	def get_ref_subframe(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:POWC:REFSubframe \n
		Snippet: value: int = driver.source.bb.eutra.powc.get_ref_subframe() \n
		If BB:EUTRa:POWC:LEVReferenceUEBurst, queries the subframe or slot number used as reference for measuring the RMS and PEP
		values. \n
			:return: ref_subframe: integer Range: 0 to 39
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:POWC:REFSubframe?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_rue(self) -> enums.EutraMobStatType:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:POWC:RUE \n
		Snippet: value: enums.EutraMobStatType = driver.source.bb.eutra.powc.get_rue() \n
		If BB:EUTRa:POWC:LEVReferenceUEBurst, queries the UE to that the measured RMS and PEP are referring. \n
			:return: reference_ue: UE1| UE2| UE3| UE4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:POWC:RUE?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMobStatType)
