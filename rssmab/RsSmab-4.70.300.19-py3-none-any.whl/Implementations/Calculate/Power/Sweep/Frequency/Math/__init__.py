from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Math:
	"""Math commands group definition. 2 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: Math, default value after init: Math.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("math", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_math_get', 'repcap_math_set', repcap.Math.Nr1)

	def repcap_math_set(self, math: repcap.Math) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Math.Default
		Default value after init: Math.Nr1"""
		self._cmd_group.set_repcap_enum_value(math)

	def repcap_math_get(self) -> repcap.Math:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def subtract(self):
		"""subtract commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subtract'):
			from .Subtract import Subtract
			self._subtract = Subtract(self._core, self._cmd_group)
		return self._subtract

	def clone(self) -> 'Math':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Math(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
