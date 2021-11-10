from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rms:
	"""Rms commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rms", core, parent)

	def set(self, enable: bool, limit: float) -> None:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:LIMit:NXDN:FFERor:RMS \n
		Snippet: driver.configure.vse.measurement.limit.nxdn.ffError.rms.set(enable = False, limit = 1.0) \n
		Enables/disables limit evaluation and sets the upper limit for the RMS FSK frequency error. \n
			:param enable: OFF | ON
			:param limit: Range: 0 FS to 1 FS, Unit: %
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('limit', limit, DataType.Float))
		self._core.io.write(f'CONFigure:VSE:MEASurement<Instance>:LIMit:NXDN:FFERor:RMS {param}'.rstrip())

	# noinspection PyTypeChecker
	class RmsStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF | ON
			- Limit: float: Range: 0 FS to 1 FS, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get(self) -> RmsStruct:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:LIMit:NXDN:FFERor:RMS \n
		Snippet: value: RmsStruct = driver.configure.vse.measurement.limit.nxdn.ffError.rms.get() \n
		Enables/disables limit evaluation and sets the upper limit for the RMS FSK frequency error. \n
			:return: structure: for return value, see the help for RmsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:VSE:MEASurement<Instance>:LIMit:NXDN:FFERor:RMS?', self.__class__.RmsStruct())
