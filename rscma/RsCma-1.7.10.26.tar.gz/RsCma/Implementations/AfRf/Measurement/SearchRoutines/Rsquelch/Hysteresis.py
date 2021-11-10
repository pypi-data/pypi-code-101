from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hysteresis:
	"""Hysteresis commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hysteresis", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:AFRF:MEASurement<Instance>:SROutines:RSQuelch:HYSTeresis \n
		Snippet: value: float = driver.afRf.measurement.searchRoutines.rsquelch.hysteresis.fetch() \n
		Fetches the difference between the off level and the on level. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: hysteresis: Range: 0 dB to 50 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:AFRF:MEASurement<Instance>:SROutines:RSQuelch:HYSTeresis?', suppressed)
		return Conversions.str_to_float(response)

	def calculate(self) -> float or bool:
		"""SCPI: CALCulate:AFRF:MEASurement<Instance>:SROutines:RSQuelch:HYSTeresis \n
		Snippet: value: float or bool = driver.afRf.measurement.searchRoutines.rsquelch.hysteresis.calculate() \n
		Fetches the difference between the off level and the on level. \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: hysteresis: (float or boolean) Range: 0 dB to 50 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:AFRF:MEASurement<Instance>:SROutines:RSQuelch:HYSTeresis?', suppressed)
		return Conversions.str_to_float_or_bool(response)

	def read(self) -> float:
		"""SCPI: READ:AFRF:MEASurement<Instance>:SROutines:RSQuelch:HYSTeresis \n
		Snippet: value: float = driver.afRf.measurement.searchRoutines.rsquelch.hysteresis.read() \n
		No command help available \n
		Use RsCma.reliability.last_value to read the updated reliability indicator. \n
			:return: hysteresis: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:AFRF:MEASurement<Instance>:SROutines:RSQuelch:HYSTeresis?', suppressed)
		return Conversions.str_to_float(response)
