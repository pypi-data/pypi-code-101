from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:EXECute \n
		Snippet: driver.source.bb.arbitrary.mcarrier.edit.carrier.execute.set() \n
		The command adopts the settings for the carrier range which has been defined using the BB:ARB:MCAR:EDIT:CARR:... commands. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:EXECute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:EXECute \n
		Snippet: driver.source.bb.arbitrary.mcarrier.edit.carrier.execute.set_with_opc() \n
		The command adopts the settings for the carrier range which has been defined using the BB:ARB:MCAR:EDIT:CARR:... commands. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSgt.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:EXECute', opc_timeout_ms)
