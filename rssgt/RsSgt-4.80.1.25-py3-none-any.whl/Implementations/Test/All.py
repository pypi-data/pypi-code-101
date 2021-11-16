from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	def get_result(self) -> enums.Test:
		"""SCPI: TEST:ALL:RESult \n
		Snippet: value: enums.Test = driver.test.all.get_result() \n
		Queries the result of the performed selftest. Start the selftest with method RsSgt.Test.All.start. \n
			:return: result: 0| 1| RUNning| STOPped
		"""
		response = self._core.io.query_str('TEST:ALL:RESult?')
		return Conversions.str_to_scalar_enum(response, enums.Test)

	def start(self) -> None:
		"""SCPI: TEST:ALL:STARt \n
		Snippet: driver.test.all.start() \n
		Starts the selftest. Use the command method RsSgt.Test.All.result to query the result. \n
		"""
		self._core.io.write(f'TEST:ALL:STARt')

	def start_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: TEST:ALL:STARt \n
		Snippet: driver.test.all.start_with_opc() \n
		Starts the selftest. Use the command method RsSgt.Test.All.result to query the result. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsSgt.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TEST:ALL:STARt', opc_timeout_ms)
