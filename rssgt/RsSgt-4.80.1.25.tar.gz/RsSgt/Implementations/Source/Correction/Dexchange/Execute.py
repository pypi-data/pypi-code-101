from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:EXECute \n
		Snippet: driver.source.correction.dexchange.execute.set() \n
		Starts the export or import of the selected file. When import is selected, the ASCII file is imported as user correction
		list. When export is selected, the user correction list is exported into the selected ASCII file. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:CORRection:DEXChange:EXECute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:EXECute \n
		Snippet: driver.source.correction.dexchange.execute.set_with_opc() \n
		Starts the export or import of the selected file. When import is selected, the ASCII file is imported as user correction
		list. When export is selected, the user correction list is exported into the selected ASCII file. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSgt.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:CORRection:DEXChange:EXECute', opc_timeout_ms)
