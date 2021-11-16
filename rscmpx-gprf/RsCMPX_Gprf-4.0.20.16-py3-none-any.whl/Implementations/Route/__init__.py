from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Route:
	"""Route commands group definition. 34 total commands, 9 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("route", core, parent)

	@property
	def gprf(self):
		"""gprf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gprf'):
			from .Gprf import Gprf
			self._gprf = Gprf(self._core, self._cmd_group)
		return self._gprf

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import Lte
			self._lte = Lte(self._core, self._cmd_group)
		return self._lte

	@property
	def nrMmw(self):
		"""nrMmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrMmw'):
			from .NrMmw import NrMmw
			self._nrMmw = NrMmw(self._core, self._cmd_group)
		return self._nrMmw

	@property
	def nrSub(self):
		"""nrSub commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrSub'):
			from .NrSub import NrSub
			self._nrSub = NrSub(self._core, self._cmd_group)
		return self._nrSub

	@property
	def uwb(self):
		"""uwb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uwb'):
			from .Uwb import Uwb
			self._uwb = Uwb(self._core, self._cmd_group)
		return self._uwb

	@property
	def wlan(self):
		"""wlan commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wlan'):
			from .Wlan import Wlan
			self._wlan = Wlan(self._core, self._cmd_group)
		return self._wlan

	@property
	def bluetooth(self):
		"""bluetooth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bluetooth'):
			from .Bluetooth import Bluetooth
			self._bluetooth = Bluetooth(self._core, self._cmd_group)
		return self._bluetooth

	@property
	def gsm(self):
		"""gsm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gsm'):
			from .Gsm import Gsm
			self._gsm = Gsm(self._core, self._cmd_group)
		return self._gsm

	@property
	def wcdma(self):
		"""wcdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wcdma'):
			from .Wcdma import Wcdma
			self._wcdma = Wcdma(self._core, self._cmd_group)
		return self._wcdma

	def clone(self) -> 'Route':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Route(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
