from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Xval: List[float]: No parameter help available
			- Yval: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Xval', DataType.FloatList, None, False, True, 1),
			ArgStruct('Yval', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Xval: List[float] = None
			self.Yval: List[float] = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:VSE:MEASurement<Instance>:CONS:IQ:CURRent \n
		Snippet: value: ResultData = driver.vse.measurement.cons.iq.current.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:VSE:MEASurement<Instance>:CONS:IQ:CURRent?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:VSE:MEASurement<Instance>:CONS:IQ:CURRent \n
		Snippet: value: ResultData = driver.vse.measurement.cons.iq.current.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:VSE:MEASurement<Instance>:CONS:IQ:CURRent?', self.__class__.ResultData())
