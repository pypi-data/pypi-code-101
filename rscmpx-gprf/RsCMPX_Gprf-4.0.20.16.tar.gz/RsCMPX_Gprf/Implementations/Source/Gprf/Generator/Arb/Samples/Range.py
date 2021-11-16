from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, range_py: enums.Range, start: int = None, stop: int = None) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SAMPles:RANGe \n
		Snippet: driver.source.gprf.generator.arb.samples.range.set(range_py = enums.Range.FULL, start = 1, stop = 1) \n
		Defines the range of samples in the loaded ARB file that are processed. \n
			:param range_py: FULL: The full ARB file is processed. SUB: The subrange defined by the Start and Stop parameters is processed.
			:param start: The beginning (first sample) of the subrange.
			:param stop: The end (last sample) of the subrange.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('range_py', range_py, DataType.Enum, enums.Range), ArgSingle('start', start, DataType.Integer, None, is_optional=True), ArgSingle('stop', stop, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:SAMPles:RANGe {param}'.rstrip())

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Response structure. Fields: \n
			- Range_Py: enums.Range: FULL: The full ARB file is processed. SUB: The subrange defined by the Start and Stop parameters is processed.
			- Start: int: The beginning (first sample) of the subrange.
			- Stop: int: The end (last sample) of the subrange."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Range_Py', enums.Range),
			ArgStruct.scalar_int('Start'),
			ArgStruct.scalar_int('Stop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Range_Py: enums.Range = None
			self.Start: int = None
			self.Stop: int = None

	def get(self) -> RangeStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SAMPles:RANGe \n
		Snippet: value: RangeStruct = driver.source.gprf.generator.arb.samples.range.get() \n
		Defines the range of samples in the loaded ARB file that are processed. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:ARB:SAMPles:RANGe?', self.__class__.RangeStruct())
