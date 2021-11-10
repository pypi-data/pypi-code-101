from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:AFRF:MEASurement<Instance>:DATA:FSK:BERate:CURRent \n
		Snippet: value: int = driver.afRf.measurement.data.fsk.bitErrorRate.current.fetch() \n
		Fetches the bit error rate result. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: ber: Range: 0 to 100"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:AFRF:MEASurement<Instance>:DATA:FSK:BERate:CURRent?', suppressed)
		return Conversions.str_to_int(response)
