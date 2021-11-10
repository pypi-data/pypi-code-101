from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, enable: bool, upper: float) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:LIMit:TSENsitivity:AOUT:LEVel \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.limit.tsensitivity.audioOutput.level.set(enable = False, upper = 1.0) \n
		No command help available \n
			:param enable: No help available
			:param upper: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('upper', upper, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:LIMit:TSENsitivity:AOUT:LEVel {param}'.rstrip())

	# noinspection PyTypeChecker
	class LevelStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: No parameter help available
			- Upper: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper: float = None

	def get(self) -> LevelStruct:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:LIMit:TSENsitivity:AOUT:LEVel \n
		Snippet: value: LevelStruct = driver.configure.afRf.measurement.searchRoutines.limit.tsensitivity.audioOutput.level.get() \n
		No command help available \n
			:return: structure: for return value, see the help for LevelStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:LIMit:TSENsitivity:AOUT:LEVel?', self.__class__.LevelStruct())
