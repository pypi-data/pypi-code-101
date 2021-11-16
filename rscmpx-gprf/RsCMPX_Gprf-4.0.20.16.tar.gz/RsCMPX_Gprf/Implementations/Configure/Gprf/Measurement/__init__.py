from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 163 total commands, 12 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenario'):
			from .Scenario import Scenario
			self._scenario = Scenario(self._core, self._cmd_group)
		return self._scenario

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def correction(self):
		"""correction commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 7 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def iqVsSlot(self):
		"""iqVsSlot commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_iqVsSlot'):
			from .IqVsSlot import IqVsSlot
			self._iqVsSlot = IqVsSlot(self._core, self._cmd_group)
		return self._iqVsSlot

	@property
	def extPwrSensor(self):
		"""extPwrSensor commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_extPwrSensor'):
			from .ExtPwrSensor import ExtPwrSensor
			self._extPwrSensor = ExtPwrSensor(self._core, self._cmd_group)
		return self._extPwrSensor

	@property
	def nrpm(self):
		"""nrpm commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_nrpm'):
			from .Nrpm import Nrpm
			self._nrpm = Nrpm(self._core, self._cmd_group)
		return self._nrpm

	@property
	def iqRecorder(self):
		"""iqRecorder commands group. 5 Sub-classes, 10 commands."""
		if not hasattr(self, '_iqRecorder'):
			from .IqRecorder import IqRecorder
			self._iqRecorder = IqRecorder(self._core, self._cmd_group)
		return self._iqRecorder

	@property
	def spectrum(self):
		"""spectrum commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._cmd_group)
		return self._spectrum

	@property
	def fftSpecAn(self):
		"""fftSpecAn commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_fftSpecAn'):
			from .FftSpecAn import FftSpecAn
			self._fftSpecAn = FftSpecAn(self._core, self._cmd_group)
		return self._fftSpecAn

	@property
	def ploss(self):
		"""ploss commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_ploss'):
			from .Ploss import Ploss
			self._ploss = Ploss(self._core, self._cmd_group)
		return self._ploss

	@property
	def canalyzer(self):
		"""canalyzer commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_canalyzer'):
			from .Canalyzer import Canalyzer
			self._canalyzer = Canalyzer(self._core, self._cmd_group)
		return self._canalyzer

	# noinspection PyTypeChecker
	def get_display(self) -> enums.MeasTab:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:DISPlay \n
		Snippet: value: enums.MeasTab = driver.configure.gprf.measurement.get_display() \n
		No command help available \n
			:return: meas_tab: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:DISPlay?')
		return Conversions.str_to_scalar_enum(response, enums.MeasTab)

	def set_display(self, meas_tab: enums.MeasTab) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:DISPlay \n
		Snippet: driver.configure.gprf.measurement.set_display(meas_tab = enums.MeasTab.EPSensor) \n
		No command help available \n
			:param meas_tab: No help available
		"""
		param = Conversions.enum_scalar_to_str(meas_tab, enums.MeasTab)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:DISPlay {param}')

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
