from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Command:
	"""Command commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("command", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_index_get', 'repcap_index_set', repcap.Index.Nr1)

	def repcap_index_set(self, index: repcap.Index) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Index.Default
		Default value after init: Index.Nr1"""
		self._cmd_group.set_repcap_enum_value(index)

	def repcap_index_get(self) -> repcap.Index:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, index=repcap.Index.Default) -> None:
		"""SCPI: TSGen:CONFigure:COMMand<CH> \n
		Snippet: driver.tsGen.configure.command.set(index = repcap.Index.Default) \n
		Triggers playing, pausing and stopping of the TS player file selected with method RsSmcv.TsGen.Configure.playFile. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Command')
		"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'TSGen:CONFigure:COMMand{index_cmd_val}')

	def set_with_opc(self, index=repcap.Index.Default, opc_timeout_ms: int = -1) -> None:
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		"""SCPI: TSGen:CONFigure:COMMand<CH> \n
		Snippet: driver.tsGen.configure.command.set_with_opc(index = repcap.Index.Default) \n
		Triggers playing, pausing and stopping of the TS player file selected with method RsSmcv.TsGen.Configure.playFile. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Command')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TSGen:CONFigure:COMMand{index_cmd_val}', opc_timeout_ms)

	def clone(self) -> 'Command':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Command(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
