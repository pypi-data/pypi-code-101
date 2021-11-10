from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 9 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def fsk(self):
		"""fsk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fsk'):
			from .Fsk import Fsk
			self._fsk = Fsk(self._core, self._cmd_group)
		return self._fsk

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:AFRF:MEASurement<Instance>:DATA \n
		Snippet: driver.afRf.measurement.data.initiate() \n
		Starts or continues the measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:AFRF:MEASurement<Instance>:DATA', opc_timeout_ms)

	def stop(self) -> None:
		"""SCPI: STOP:AFRF:MEASurement<Instance>:DATA \n
		Snippet: driver.afRf.measurement.data.stop() \n
		Pauses the measurement. \n
		"""
		self._core.io.write(f'STOP:AFRF:MEASurement<Instance>:DATA')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:AFRF:MEASurement<Instance>:DATA \n
		Snippet: driver.afRf.measurement.data.stop_with_opc() \n
		Pauses the measurement. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCma.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:AFRF:MEASurement<Instance>:DATA', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:AFRF:MEASurement<Instance>:DATA \n
		Snippet: driver.afRf.measurement.data.abort() \n
		Stops the measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:AFRF:MEASurement<Instance>:DATA', opc_timeout_ms)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
