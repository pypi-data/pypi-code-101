from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class End:
	"""End commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("end", core, parent)

	def set(self) -> None:
		"""SCPI: CALibration:AINPut:END \n
		Snippet: driver.calibration.ainput.end.set() \n
		Ends the analog input adjustment. \n
		"""
		self._core.io.write(f'CALibration:AINPut:END')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALibration:AINPut:END \n
		Snippet: driver.calibration.ainput.end.set_with_opc() \n
		Ends the analog input adjustment. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALibration:AINPut:END', opc_timeout_ms)
