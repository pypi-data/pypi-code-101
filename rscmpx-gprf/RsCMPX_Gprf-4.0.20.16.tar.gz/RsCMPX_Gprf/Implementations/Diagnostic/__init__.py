from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Diagnostic:
	"""Diagnostic commands group definition. 32 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("diagnostic", core, parent)

	@property
	def gprf(self):
		"""gprf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gprf'):
			from .Gprf import Gprf
			self._gprf = Gprf(self._core, self._cmd_group)
		return self._gprf

	@property
	def generic(self):
		"""generic commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_generic'):
			from .Generic import Generic
			self._generic = Generic(self._core, self._cmd_group)
		return self._generic

	@property
	def meas(self):
		"""meas commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_meas'):
			from .Meas import Meas
			self._meas = Meas(self._core, self._cmd_group)
		return self._meas

	@property
	def route(self):
		"""route commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_route'):
			from .Route import Route
			self._route = Route(self._core, self._cmd_group)
		return self._route

	@property
	def trigger(self):
		"""trigger commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	def clone(self) -> 'Diagnostic':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Diagnostic(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
