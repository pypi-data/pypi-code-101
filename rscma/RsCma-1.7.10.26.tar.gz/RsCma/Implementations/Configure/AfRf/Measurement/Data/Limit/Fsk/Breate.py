from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Breate:
	"""Breate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("breate", core, parent)

	def set(self, enable_limit: bool, lower: int, upper: int) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:LIMit:FSK:BREate \n
		Snippet: driver.configure.afRf.measurement.data.limit.fsk.breate.set(enable_limit = False, lower = 1, upper = 1) \n
		Enables a limit check and sets the upper limit for the bit error rate. \n
			:param enable_limit: OFF | ON Range: 0 to 100
			:param lower: Range: 0 to 100
			:param upper: Range: -130 dBm to 55 dBm, Unit: dBm
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable_limit', enable_limit, DataType.Boolean), ArgSingle('lower', lower, DataType.Integer), ArgSingle('upper', upper, DataType.Integer))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DATA:LIMit:FSK:BREate {param}'.rstrip())

	# noinspection PyTypeChecker
	class BreateStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable_Limit: bool: OFF | ON Range: 0 to 100
			- Lower: int: Range: 0 to 100
			- Upper: int: Range: -130 dBm to 55 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Limit'),
			ArgStruct.scalar_int('Lower'),
			ArgStruct.scalar_int('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Limit: bool = None
			self.Lower: int = None
			self.Upper: int = None

	def get(self) -> BreateStruct:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:LIMit:FSK:BREate \n
		Snippet: value: BreateStruct = driver.configure.afRf.measurement.data.limit.fsk.breate.get() \n
		Enables a limit check and sets the upper limit for the bit error rate. \n
			:return: structure: for return value, see the help for BreateStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:DATA:LIMit:FSK:BREate?', self.__class__.BreateStruct())
