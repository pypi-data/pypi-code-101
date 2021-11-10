from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Object:
	"""Object commands group definition. 7 total commands, 6 Sub-groups, 0 group commands
	Repeated Capability: ObjectIx, default value after init: ObjectIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("object", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_objectIx_get', 'repcap_objectIx_set', repcap.ObjectIx.Nr1)

	def repcap_objectIx_set(self, objectIx: repcap.ObjectIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ObjectIx.Default
		Default value after init: ObjectIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(objectIx)

	def repcap_objectIx_get(self) -> repcap.ObjectIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def attenuation(self):
		"""attenuation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attenuation'):
			from .Attenuation import Attenuation
			self._attenuation = Attenuation(self._core, self._cmd_group)
		return self._attenuation

	@property
	def doppler(self):
		"""doppler commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_doppler'):
			from .Doppler import Doppler
			self._doppler = Doppler(self._core, self._cmd_group)
		return self._doppler

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	@property
	def rcs(self):
		"""rcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcs'):
			from .Rcs import Rcs
			self._rcs = Rcs(self._core, self._cmd_group)
		return self._rcs

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Object':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Object(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
