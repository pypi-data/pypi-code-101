from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Socket:
	"""Socket commands group definition. 3 total commands, 3 Sub-groups, 0 group commands
	Repeated Capability: SocketInstance, default value after init: SocketInstance.Inst1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("socket", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_socketInstance_get', 'repcap_socketInstance_set', repcap.SocketInstance.Inst1)

	def repcap_socketInstance_set(self, socketInstance: repcap.SocketInstance) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SocketInstance.Default
		Default value after init: SocketInstance.Inst1"""
		self._cmd_group.set_repcap_enum_value(socketInstance)

	def repcap_socketInstance_get(self) -> repcap.SocketInstance:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def vresource(self):
		"""vresource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vresource'):
			from .Vresource import Vresource
			self._vresource = Vresource(self._core, self._cmd_group)
		return self._vresource

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Port import Port
			self._port = Port(self._core, self._cmd_group)
		return self._port

	def clone(self) -> 'Socket':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Socket(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
