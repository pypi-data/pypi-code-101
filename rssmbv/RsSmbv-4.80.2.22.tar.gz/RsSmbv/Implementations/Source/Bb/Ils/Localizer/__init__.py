from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Localizer:
	"""Localizer commands group definition. 28 total commands, 6 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("localizer", core, parent)

	@property
	def comid(self):
		"""comid commands group. 1 Sub-classes, 10 commands."""
		if not hasattr(self, '_comid'):
			from .Comid import Comid
			self._comid = Comid(self._core, self._cmd_group)
		return self._comid

	@property
	def ddm(self):
		"""ddm commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_ddm'):
			from .Ddm import Ddm
			self._ddm = Ddm(self._core, self._cmd_group)
		return self._ddm

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def icao(self):
		"""icao commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icao'):
			from .Icao import Icao
			self._icao = Icao(self._core, self._cmd_group)
		return self._icao

	@property
	def llobe(self):
		"""llobe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_llobe'):
			from .Llobe import Llobe
			self._llobe = Llobe(self._core, self._cmd_group)
		return self._llobe

	@property
	def rlobe(self):
		"""rlobe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlobe'):
			from .Rlobe import Rlobe
			self._rlobe = Rlobe(self._core, self._cmd_group)
		return self._rlobe

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AvionicIlsLocMode:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:LOCalizer:MODE \n
		Snippet: value: enums.AvionicIlsLocMode = driver.source.bb.ils.localizer.get_mode() \n
		Sets the operating mode for the ILS localizer modulation signal. \n
			:return: mode: NORM| LLOBe| RLOBe NORM ILS localizer modulation is active. LLOBe Amplitude modulation of the output signal with the left lobe (90Hz) signal component of the ILS localizer signal is active. RLOBe Amplitude modulation of the output signal with the right lobe (150Hz) signal component of the ILS localizer signal is active.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ILS:LOCalizer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AvionicIlsLocMode)

	def set_mode(self, mode: enums.AvionicIlsLocMode) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:LOCalizer:MODE \n
		Snippet: driver.source.bb.ils.localizer.set_mode(mode = enums.AvionicIlsLocMode.LLOBe) \n
		Sets the operating mode for the ILS localizer modulation signal. \n
			:param mode: NORM| LLOBe| RLOBe NORM ILS localizer modulation is active. LLOBe Amplitude modulation of the output signal with the left lobe (90Hz) signal component of the ILS localizer signal is active. RLOBe Amplitude modulation of the output signal with the right lobe (150Hz) signal component of the ILS localizer signal is active.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AvionicIlsLocMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ILS:LOCalizer:MODE {param}')

	def get_phase(self) -> float:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:LOCalizer:PHASe \n
		Snippet: value: float = driver.source.bb.ils.localizer.get_phase() \n
		Sets the phase between the modulation signals of the left and right antenna lobe of the ILS localizer signal. The zero
		crossing of the right lobe (150 Hz) signal serves as a reference. The angle refers to the period of the signal of the
		right antenna lobe. \n
			:return: phase: float Range: -60 to 120
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ILS:LOCalizer:PHASe?')
		return Conversions.str_to_float(response)

	def set_phase(self, phase: float) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:LOCalizer:PHASe \n
		Snippet: driver.source.bb.ils.localizer.set_phase(phase = 1.0) \n
		Sets the phase between the modulation signals of the left and right antenna lobe of the ILS localizer signal. The zero
		crossing of the right lobe (150 Hz) signal serves as a reference. The angle refers to the period of the signal of the
		right antenna lobe. \n
			:param phase: float Range: -60 to 120
		"""
		param = Conversions.decimal_value_to_str(phase)
		self._core.io.write(f'SOURce<HwInstance>:BB:ILS:LOCalizer:PHASe {param}')

	def get_sdm(self) -> float:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:LOCalizer:SDM \n
		Snippet: value: float = driver.source.bb.ils.localizer.get_sdm() \n
		Sets the arithmetic sum of the modulation depths of the left lobe (90 Hz) and right lobe (150 Hz) for the ILS localizer
		signal contents. The RMS modulation depth of the sum signal depends on the phase setting of both modulation tones. \n
			:return: sdm: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ILS:LOCalizer:SDM?')
		return Conversions.str_to_float(response)

	def set_sdm(self, sdm: float) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:LOCalizer:SDM \n
		Snippet: driver.source.bb.ils.localizer.set_sdm(sdm = 1.0) \n
		Sets the arithmetic sum of the modulation depths of the left lobe (90 Hz) and right lobe (150 Hz) for the ILS localizer
		signal contents. The RMS modulation depth of the sum signal depends on the phase setting of both modulation tones. \n
			:param sdm: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(sdm)
		self._core.io.write(f'SOURce<HwInstance>:BB:ILS:LOCalizer:SDM {param}')

	def clone(self) -> 'Localizer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Localizer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
