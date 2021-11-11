from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, arg_0: List[int], arg_1: List[float], arg_2: List[float]) -> None:
		"""SCPI: BATTery:MODel:DATA \n
		Snippet: driver.battery.model.data.set(arg_0 = [1, 2, 3], arg_1 = [1.1, 2.2, 3.3], arg_2 = [1.1, 2.2, 3.3]) \n
		Sets or queries the battery model data. \n
			:param arg_0: Sets the value for battery state of charge (SoC) .
			:param arg_1: Sets the value for battery open-circuit voltage (Voc) .
			:param arg_2: Sets the value for battery internal resistance (ESR) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('arg_0', arg_0, DataType.IntegerList, None), ArgSingle.as_open_list('arg_1', arg_1, DataType.FloatList, None), ArgSingle.as_open_list('arg_2', arg_2, DataType.FloatList, None))
		self._core.io.write(f'BATTery:MODel:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: List[int]: Sets the value for battery state of charge (SoC) .
			- Arg_1: List[float]: Sets the value for battery open-circuit voltage (Voc) .
			- Arg_2: List[float]: Sets the value for battery internal resistance (ESR) ."""
		__meta_args_list = [
			ArgStruct('Arg_0', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Arg_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Arg_2', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: List[int] = None
			self.Arg_1: List[float] = None
			self.Arg_2: List[float] = None

	def get(self) -> DataStruct:
		"""SCPI: BATTery:MODel:DATA \n
		Snippet: value: DataStruct = driver.battery.model.data.get() \n
		Sets or queries the battery model data. \n
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		return self._core.io.query_struct(f'BATTery:MODel:DATA?', self.__class__.DataStruct())
