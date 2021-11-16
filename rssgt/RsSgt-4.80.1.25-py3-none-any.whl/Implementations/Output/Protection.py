from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Protection:
	"""Protection commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("protection", core, parent)

	def clear(self) -> None:
		"""SCPI: OUTPut<HW>:PROTection:CLEar \n
		Snippet: driver.output.protection.clear() \n
		No command help available \n
		"""
		self._core.io.write(f'OUTPut<HwInstance>:PROTection:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: OUTPut<HW>:PROTection:CLEar \n
		Snippet: driver.output.protection.clear_with_opc() \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSgt.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'OUTPut<HwInstance>:PROTection:CLEar', opc_timeout_ms)
