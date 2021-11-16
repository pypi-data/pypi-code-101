from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 43 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def iqVsSlot(self):
		"""iqVsSlot commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_iqVsSlot'):
			from .IqVsSlot import IqVsSlot
			self._iqVsSlot = IqVsSlot(self._core, self._cmd_group)
		return self._iqVsSlot

	@property
	def iqRecorder(self):
		"""iqRecorder commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_iqRecorder'):
			from .IqRecorder import IqRecorder
			self._iqRecorder = IqRecorder(self._core, self._cmd_group)
		return self._iqRecorder

	@property
	def spectrum(self):
		"""spectrum commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._cmd_group)
		return self._spectrum

	@property
	def fftSpecAn(self):
		"""fftSpecAn commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_fftSpecAn'):
			from .FftSpecAn import FftSpecAn
			self._fftSpecAn = FftSpecAn(self._core, self._cmd_group)
		return self._fftSpecAn

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
