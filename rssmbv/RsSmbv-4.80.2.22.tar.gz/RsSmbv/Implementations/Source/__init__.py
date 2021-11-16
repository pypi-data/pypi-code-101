from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 8316 total commands, 32 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	@property
	def adf(self):
		"""adf commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_adf'):
			from .Adf import Adf
			self._adf = Adf(self._core, self._cmd_group)
		return self._adf

	@property
	def am(self):
		"""am commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_am'):
			from .Am import Am
			self._am = Am(self._core, self._cmd_group)
		return self._am

	@property
	def awgn(self):
		"""awgn commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import Awgn
			self._awgn = Awgn(self._core, self._cmd_group)
		return self._awgn

	@property
	def bb(self):
		"""bb commands group. 35 Sub-classes, 6 commands."""
		if not hasattr(self, '_bb'):
			from .Bb import Bb
			self._bb = Bb(self._core, self._cmd_group)
		return self._bb

	@property
	def bbin(self):
		"""bbin commands group. 7 Sub-classes, 9 commands."""
		if not hasattr(self, '_bbin'):
			from .Bbin import Bbin
			self._bbin = Bbin(self._core, self._cmd_group)
		return self._bbin

	@property
	def combined(self):
		"""combined commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_combined'):
			from .Combined import Combined
			self._combined = Combined(self._core, self._cmd_group)
		return self._combined

	@property
	def correction(self):
		"""correction commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def dm(self):
		"""dm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dm'):
			from .Dm import Dm
			self._dm = Dm(self._core, self._cmd_group)
		return self._dm

	@property
	def dme(self):
		"""dme commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_dme'):
			from .Dme import Dme
			self._dme = Dme(self._core, self._cmd_group)
		return self._dme

	@property
	def fm(self):
		"""fm commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_fm'):
			from .Fm import Fm
			self._fm = Fm(self._core, self._cmd_group)
		return self._fm

	@property
	def frequency(self):
		"""frequency commands group. 4 Sub-classes, 9 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def freqSweep(self):
		"""freqSweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqSweep'):
			from .FreqSweep import FreqSweep
			self._freqSweep = FreqSweep(self._core, self._cmd_group)
		return self._freqSweep

	@property
	def ils(self):
		"""ils commands group. 7 Sub-classes, 2 commands."""
		if not hasattr(self, '_ils'):
			from .Ils import Ils
			self._ils = Ils(self._core, self._cmd_group)
		return self._ils

	@property
	def inputPy(self):
		"""inputPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def iq(self):
		"""iq commands group. 6 Sub-classes, 5 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def lffSweep(self):
		"""lffSweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lffSweep'):
			from .LffSweep import LffSweep
			self._lffSweep = LffSweep(self._core, self._cmd_group)
		return self._lffSweep

	@property
	def lfOutput(self):
		"""lfOutput commands group. 8 Sub-classes, 3 commands."""
		if not hasattr(self, '_lfOutput'):
			from .LfOutput import LfOutput
			self._lfOutput = LfOutput(self._core, self._cmd_group)
		return self._lfOutput

	@property
	def listPy(self):
		"""listPy commands group. 8 Sub-classes, 8 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def mbeacon(self):
		"""mbeacon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mbeacon'):
			from .Mbeacon import Mbeacon
			self._mbeacon = Mbeacon(self._core, self._cmd_group)
		return self._mbeacon

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def noise(self):
		"""noise commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_noise'):
			from .Noise import Noise
			self._noise = Noise(self._core, self._cmd_group)
		return self._noise

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	@property
	def pgenerator(self):
		"""pgenerator commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pgenerator'):
			from .Pgenerator import Pgenerator
			self._pgenerator = Pgenerator(self._core, self._cmd_group)
		return self._pgenerator

	@property
	def phase(self):
		"""phase commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def pm(self):
		"""pm commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_pm'):
			from .Pm import Pm
			self._pm = Pm(self._core, self._cmd_group)
		return self._pm

	@property
	def power(self):
		"""power commands group. 8 Sub-classes, 10 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def psweep(self):
		"""psweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_psweep'):
			from .Psweep import Psweep
			self._psweep = Psweep(self._core, self._cmd_group)
		return self._psweep

	@property
	def pulm(self):
		"""pulm commands group. 3 Sub-classes, 9 commands."""
		if not hasattr(self, '_pulm'):
			from .Pulm import Pulm
			self._pulm = Pulm(self._core, self._cmd_group)
		return self._pulm

	@property
	def roscillator(self):
		"""roscillator commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_roscillator'):
			from .Roscillator import Roscillator
			self._roscillator = Roscillator(self._core, self._cmd_group)
		return self._roscillator

	@property
	def sweep(self):
		"""sweep commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	@property
	def valRf(self):
		"""valRf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_valRf'):
			from .ValRf import ValRf
			self._valRf = ValRf(self._core, self._cmd_group)
		return self._valRf

	@property
	def vor(self):
		"""vor commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_vor'):
			from .Vor import Vor
			self._vor = Vor(self._core, self._cmd_group)
		return self._vor

	def preset(self) -> None:
		"""SCPI: SOURce<HW>:PRESet \n
		Snippet: driver.source.preset() \n
		Presets all parameters which are related to the selected signal path. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SOURce<HW>:PRESet \n
		Snippet: driver.source.preset_with_opc() \n
		Presets all parameters which are related to the selected signal path. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmbv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:PRESet', opc_timeout_ms)

	def clone(self) -> 'Source':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Source(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
