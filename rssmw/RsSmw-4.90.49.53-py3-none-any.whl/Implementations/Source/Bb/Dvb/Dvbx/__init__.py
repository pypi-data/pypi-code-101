from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dvbx:
	"""Dvbx commands group definition. 63 total commands, 14 Sub-groups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dvbx", core, parent)

	@property
	def adLength(self):
		"""adLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adLength'):
			from .AdLength import AdLength
			self._adLength = AdLength(self._core, self._cmd_group)
		return self._adLength

	@property
	def bhConfig(self):
		"""bhConfig commands group. 5 Sub-classes, 4 commands."""
		if not hasattr(self, '_bhConfig'):
			from .BhConfig import BhConfig
			self._bhConfig = BhConfig(self._core, self._cmd_group)
		return self._bhConfig

	@property
	def binterleaver(self):
		"""binterleaver commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_binterleaver'):
			from .Binterleaver import Binterleaver
			self._binterleaver = Binterleaver(self._core, self._cmd_group)
		return self._binterleaver

	@property
	def bscrambler(self):
		"""bscrambler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bscrambler'):
			from .Bscrambler import Bscrambler
			self._bscrambler = Bscrambler(self._core, self._cmd_group)
		return self._bscrambler

	@property
	def crc(self):
		"""crc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crc'):
			from .Crc import Crc
			self._crc = Crc(self._core, self._cmd_group)
		return self._crc

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def ghConfig(self):
		"""ghConfig commands group. 7 Sub-classes, 4 commands."""
		if not hasattr(self, '_ghConfig'):
			from .GhConfig import GhConfig
			self._ghConfig = GhConfig(self._core, self._cmd_group)
		return self._ghConfig

	@property
	def icoder(self):
		"""icoder commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_icoder'):
			from .Icoder import Icoder
			self._icoder = Icoder(self._core, self._cmd_group)
		return self._icoder

	@property
	def mtab(self):
		"""mtab commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mtab'):
			from .Mtab import Mtab
			self._mtab = Mtab(self._core, self._cmd_group)
		return self._mtab

	@property
	def ocoder(self):
		"""ocoder commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ocoder'):
			from .Ocoder import Ocoder
			self._ocoder = Ocoder(self._core, self._cmd_group)
		return self._ocoder

	@property
	def pscrambler(self):
		"""pscrambler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pscrambler'):
			from .Pscrambler import Pscrambler
			self._pscrambler = Pscrambler(self._core, self._cmd_group)
		return self._pscrambler

	@property
	def pstate(self):
		"""pstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pstate'):
			from .Pstate import Pstate
			self._pstate = Pstate(self._core, self._cmd_group)
		return self._pstate

	@property
	def thConfig(self):
		"""thConfig commands group. 4 Sub-classes, 5 commands."""
		if not hasattr(self, '_thConfig'):
			from .ThConfig import ThConfig
			self._thConfig = ThConfig(self._core, self._cmd_group)
		return self._thConfig

	@property
	def ucMode(self):
		"""ucMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ucMode'):
			from .UcMode import UcMode
			self._ucMode = UcMode(self._core, self._cmd_group)
		return self._ucMode

	# noinspection PyTypeChecker
	def get_ctype(self) -> enums.DvbS2XcodeType:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:CTYPe \n
		Snippet: value: enums.DvbS2XcodeType = driver.source.bb.dvb.dvbx.get_ctype() \n
		Selects the code type. \n
			:return: ctype: NORMal| MEDium| SHORt
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XcodeType)

	def set_ctype(self, ctype: enums.DvbS2XcodeType) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:CTYPe \n
		Snippet: driver.source.bb.dvb.dvbx.set_ctype(ctype = enums.DvbS2XcodeType.MEDium) \n
		Selects the code type. \n
			:param ctype: NORMal| MEDium| SHORt
		"""
		param = Conversions.enum_scalar_to_str(ctype, enums.DvbS2XcodeType)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:CTYPe {param}')

	def get_frames(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:FRAMes \n
		Snippet: value: int = driver.source.bb.dvb.dvbx.get_frames() \n
		Sets the number of the transmitted frames. \n
			:return: frames: integer Range: 1 to UINT_MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:FRAMes?')
		return Conversions.str_to_int(response)

	def set_frames(self, frames: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:FRAMes \n
		Snippet: driver.source.bb.dvb.dvbx.set_frames(frames = 1) \n
		Sets the number of the transmitted frames. \n
			:param frames: integer Range: 1 to UINT_MAX
		"""
		param = Conversions.decimal_value_to_str(frames)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:FRAMes {param}')

	def get_istream(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:ISTReam \n
		Snippet: value: str = driver.source.bb.dvb.dvbx.get_istream() \n
		Queries the input stream type. \n
			:return: istream: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:ISTReam?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_mcod(self) -> enums.DvbS2XmodCod:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MCOD \n
		Snippet: value: enums.DvbS2XmodCod = driver.source.bb.dvb.dvbx.get_mcod() \n
		Selects the MODCOD. \n
			:return: mod_cod: QPSK_S_14| QPSK_S_13| QPSK_S_25| QPSK_S_12| QPSK_S_35| QPSK_S_23| QPSK_S_34| QPSK_S_45| QPSK_S_56| QPSK_S_89| QPSK_S_910| PSK8_S_35| PSK8_S_23| PSK8_S_34| PSK8_S_56| PSK8_S_89| PSK8_S_910| APSK16_S_23| APSK16_S_34| APSK16_S_45| APSK16_S_56| APSK16_S_89| APSK16_S_910| APSK32_S_34| APSK32_S_45| APSK32_S_56| APSK32_S_89| APSK32_S_910| QPSK_X_N1345| QPSK_X_N920| QPSK_X_N1120| APSK8_X_N59L| APSK8_X_N2645L| PSK8_X_N2336| PSK8_X_N2536| PSK8_X_N1318| APSK16_X_N12L| APSK16_X_N815L| APSK16_X_N59L| APSK16_X_N2645| APSK16_X_N35| APSK16_X_N35L| APSK16_X_N2845| APSK16_X_N2336| APSK16_X_N23L| APSK16_X_N2536| APSK16_X_N1318| APSK16_X_N79| APSK16_X_N7790| APSK32_X_N23L| APSK32_X_N3245| APSK32_X_N1115| APSK32_X_N79| APSK64_X_N3245L| APSK64_X_N1115| APSK64_X_N79| APSK64_X_N45| APSK64_X_N56| APSK128_X_N34| APSK128_X_N79| APSK256_X_N2945L| APSK256_X_N23L| APSK256_X_N3145L| APSK256_X_N3245| APSK256_X_N1115L| APSK256_X_N34| QPSK_X_S1145| QPSK_X_S415| QPSK_X_S1445| QPSK_X_S715| QPSK_X_S815| QPSK_X_S3245| PSK8_X_S715| PSK8_X_S815| PSK8_X_S2645| PSK8_X_S3245| APSK16_X_S715| APSK16_X_S815| APSK16_X_S2645| APSK16_X_S35| APSK16_X_S3245| APSK32_X_S23| APSK32_X_S3245| QPSK_X_VN29| BPSK_X_VM15| BPSK_X_VM1145| BPSK_X_VM13| BPSK_X_VS15S| BPSK_X_VS1145| BPSK_X_VS15| BPSK_X_VS415| BPSK_X_VS13
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:MCOD?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XmodCod)

	def set_mcod(self, mod_cod: enums.DvbS2XmodCod) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MCOD \n
		Snippet: driver.source.bb.dvb.dvbx.set_mcod(mod_cod = enums.DvbS2XmodCod.APSK128_X_N34) \n
		Selects the MODCOD. \n
			:param mod_cod: QPSK_S_14| QPSK_S_13| QPSK_S_25| QPSK_S_12| QPSK_S_35| QPSK_S_23| QPSK_S_34| QPSK_S_45| QPSK_S_56| QPSK_S_89| QPSK_S_910| PSK8_S_35| PSK8_S_23| PSK8_S_34| PSK8_S_56| PSK8_S_89| PSK8_S_910| APSK16_S_23| APSK16_S_34| APSK16_S_45| APSK16_S_56| APSK16_S_89| APSK16_S_910| APSK32_S_34| APSK32_S_45| APSK32_S_56| APSK32_S_89| APSK32_S_910| QPSK_X_N1345| QPSK_X_N920| QPSK_X_N1120| APSK8_X_N59L| APSK8_X_N2645L| PSK8_X_N2336| PSK8_X_N2536| PSK8_X_N1318| APSK16_X_N12L| APSK16_X_N815L| APSK16_X_N59L| APSK16_X_N2645| APSK16_X_N35| APSK16_X_N35L| APSK16_X_N2845| APSK16_X_N2336| APSK16_X_N23L| APSK16_X_N2536| APSK16_X_N1318| APSK16_X_N79| APSK16_X_N7790| APSK32_X_N23L| APSK32_X_N3245| APSK32_X_N1115| APSK32_X_N79| APSK64_X_N3245L| APSK64_X_N1115| APSK64_X_N79| APSK64_X_N45| APSK64_X_N56| APSK128_X_N34| APSK128_X_N79| APSK256_X_N2945L| APSK256_X_N23L| APSK256_X_N3145L| APSK256_X_N3245| APSK256_X_N1115L| APSK256_X_N34| QPSK_X_S1145| QPSK_X_S415| QPSK_X_S1445| QPSK_X_S715| QPSK_X_S815| QPSK_X_S3245| PSK8_X_S715| PSK8_X_S815| PSK8_X_S2645| PSK8_X_S3245| APSK16_X_S715| APSK16_X_S815| APSK16_X_S2645| APSK16_X_S35| APSK16_X_S3245| APSK32_X_S23| APSK32_X_S3245| QPSK_X_VN29| BPSK_X_VM15| BPSK_X_VM1145| BPSK_X_VM13| BPSK_X_VS15S| BPSK_X_VS1145| BPSK_X_VS15| BPSK_X_VS415| BPSK_X_VS13
		"""
		param = Conversions.enum_scalar_to_str(mod_cod, enums.DvbS2XmodCod)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:MCOD {param}')

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.DvbS2Xmodulation:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MODulation \n
		Snippet: value: enums.DvbS2Xmodulation = driver.source.bb.dvb.dvbx.get_modulation() \n
		Selects the modulation scheme. \n
			:return: modulation: QPSK| APSK16| APSK32| PSK8| P2BPsk| APSK16_8_8| APSK32_4_12_16R| APSK64_8_16_20_20| APSK8_2_4_2| APSK32_4_8_4_16| APSK64_16_16_16_16| APSK64_4_12_20_28| APSK128| APSK256
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2Xmodulation)

	def set_modulation(self, modulation: enums.DvbS2Xmodulation) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MODulation \n
		Snippet: driver.source.bb.dvb.dvbx.set_modulation(modulation = enums.DvbS2Xmodulation.APSK128) \n
		Selects the modulation scheme. \n
			:param modulation: QPSK| APSK16| APSK32| PSK8| P2BPsk| APSK16_8_8| APSK32_4_12_16R| APSK64_8_16_20_20| APSK8_2_4_2| APSK32_4_8_4_16| APSK64_16_16_16_16| APSK64_4_12_20_28| APSK128| APSK256
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.DvbS2Xmodulation)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:MODulation {param}')

	def get_no_settings(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:NOSettings \n
		Snippet: value: int = driver.source.bb.dvb.dvbx.get_no_settings() \n
		Sets the number of PLSCODEs that can be configured. \n
			:return: settings: integer Range: 1 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:NOSettings?')
		return Conversions.str_to_int(response)

	def set_no_settings(self, settings: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:NOSettings \n
		Snippet: driver.source.bb.dvb.dvbx.set_no_settings(settings = 1) \n
		Sets the number of PLSCODEs that can be configured. \n
			:param settings: integer Range: 1 to 100
		"""
		param = Conversions.decimal_value_to_str(settings)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:NOSettings {param}')

	def get_sfactor(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:SFACtor \n
		Snippet: value: int = driver.source.bb.dvb.dvbx.get_sfactor() \n
		Sets the spreading factor. \n
			:return: sfactor: integer Range: 1 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:SFACtor?')
		return Conversions.str_to_int(response)

	def set_sfactor(self, sfactor: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:SFACtor \n
		Snippet: driver.source.bb.dvb.dvbx.set_sfactor(sfactor = 1) \n
		Sets the spreading factor. \n
			:param sfactor: integer Range: 1 to 2
		"""
		param = Conversions.decimal_value_to_str(sfactor)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:SFACtor {param}')

	def get_ssequence(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:SSEQuence \n
		Snippet: value: int = driver.source.bb.dvb.dvbx.get_ssequence() \n
		Sets the bit sequence number used to scramble the pilot. \n
			:return: ssequence: integer Range: 0 to 6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:SSEQuence?')
		return Conversions.str_to_int(response)

	def set_ssequence(self, ssequence: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:SSEQuence \n
		Snippet: driver.source.bb.dvb.dvbx.set_ssequence(ssequence = 1) \n
		Sets the bit sequence number used to scramble the pilot. \n
			:param ssequence: integer Range: 0 to 6
		"""
		param = Conversions.decimal_value_to_str(ssequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:SSEQuence {param}')

	# noinspection PyTypeChecker
	def get_stype(self) -> enums.DvbS2XstmType:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:STYPe \n
		Snippet: value: enums.DvbS2XstmType = driver.source.bb.dvb.dvbx.get_stype() \n
		Selects the input stream type. \n
			:return: stype: TRANsport| GP| GC| GHEM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:STYPe?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XstmType)

	def set_stype(self, stype: enums.DvbS2XstmType) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:STYPe \n
		Snippet: driver.source.bb.dvb.dvbx.set_stype(stype = enums.DvbS2XstmType.GC) \n
		Selects the input stream type. \n
			:param stype: TRANsport| GP| GC| GHEM
		"""
		param = Conversions.enum_scalar_to_str(stype, enums.DvbS2XstmType)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:STYPe {param}')

	def get_vs_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:VSMode \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.get_vs_mode() \n
		Includes the VL-SNR (very low - signal to noise ratio) header in the physical layer frame. \n
			:return: vs_mode: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:VSMode?')
		return Conversions.str_to_bool(response)

	def set_vs_mode(self, vs_mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:VSMode \n
		Snippet: driver.source.bb.dvb.dvbx.set_vs_mode(vs_mode = False) \n
		Includes the VL-SNR (very low - signal to noise ratio) header in the physical layer frame. \n
			:param vs_mode: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(vs_mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:VSMode {param}')

	def clone(self) -> 'Dvbx':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dvbx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
