from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Date:
	"""Date commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	def set(self, year: float, month: float, day: float) -> None:
		"""SCPI: SYSTem:DATE \n
		Snippet: driver.system.date.set(year = 1.0, month = 1.0, day = 1.0) \n
		Sets or queries the system date. \n
			:param year: Sets year of the date.
			:param month: Sets month of the date.
			:param day: Sets day of the date.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('year', year, DataType.Float), ArgSingle('month', month, DataType.Float), ArgSingle('day', day, DataType.Float))
		self._core.io.write(f'SYSTem:DATE {param}'.rstrip())

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Response structure. Fields: \n
			- Year: float: Sets year of the date.
			- Month: float: Sets month of the date.
			- Day: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Year'),
			ArgStruct.scalar_float('Month'),
			ArgStruct.scalar_float('Day')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: float = None
			self.Month: float = None
			self.Day: float = None

	def get(self) -> DateStruct:
		"""SCPI: SYSTem:DATE \n
		Snippet: value: DateStruct = driver.system.date.get() \n
		Sets or queries the system date. \n
			:return: structure: for return value, see the help for DateStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:DATE?', self.__class__.DateStruct())
