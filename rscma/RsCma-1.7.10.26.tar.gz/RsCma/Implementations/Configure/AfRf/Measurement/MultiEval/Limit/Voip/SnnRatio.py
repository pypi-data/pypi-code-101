from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnnRatio:
	"""SnnRatio commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snnRatio", core, parent)

	def set(self, enable: bool, lower: float, upper: float = None) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:VOIP:SNNRatio \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.voip.snnRatio.set(enable = False, lower = 1.0, upper = 1.0) \n
		No command help available \n
			:param enable: No help available
			:param lower: No help available
			:param upper: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('lower', lower, DataType.Float), ArgSingle('upper', upper, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:VOIP:SNNRatio {param}'.rstrip())

	# noinspection PyTypeChecker
	class SnnRatioStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: No parameter help available
			- Lower: float: No parameter help available
			- Upper: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Lower: float = None
			self.Upper: float = None

	def get(self) -> SnnRatioStruct:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:VOIP:SNNRatio \n
		Snippet: value: SnnRatioStruct = driver.configure.afRf.measurement.multiEval.limit.voip.snnRatio.get() \n
		No command help available \n
			:return: structure: for return value, see the help for SnnRatioStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:VOIP:SNNRatio?', self.__class__.SnnRatioStruct())
