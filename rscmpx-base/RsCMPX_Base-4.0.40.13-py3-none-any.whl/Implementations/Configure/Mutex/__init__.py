from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mutex:
	"""Mutex commands group definition. 6 total commands, 3 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mutex", core, parent)

	@property
	def lock(self):
		"""lock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lock'):
			from .Lock import Lock
			self._lock = Lock(self._core, self._cmd_group)
		return self._lock

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def define(self):
		"""define commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_define'):
			from .Define import Define
			self._define = Define(self._core, self._cmd_group)
		return self._define

	def unlock(self, name: str, key: float) -> None:
		"""SCPI: CONFigure:MUTex:UNLock \n
		Snippet: driver.configure.mutex.unlock(name = '1', key = 1.0) \n
		No command help available \n
			:param name: No help available
			:param key: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('key', key, DataType.Float))
		self._core.io.write(f'CONFigure:MUTex:UNLock {param}'.rstrip())

	def set_undefine(self, name: str) -> None:
		"""SCPI: CONFigure:MUTex:UNDefine \n
		Snippet: driver.configure.mutex.set_undefine(name = '1') \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'CONFigure:MUTex:UNDefine {param}')

	# noinspection PyTypeChecker
	class CatalogStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Name: str: No parameter help available
			- Def_Timeout: int: No parameter help available
			- State: enums.MutexState: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Name'),
			ArgStruct.scalar_int('Def_Timeout'),
			ArgStruct.scalar_enum('State', enums.MutexState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name: str = None
			self.Def_Timeout: int = None
			self.State: enums.MutexState = None

	def get_catalog(self) -> CatalogStruct:
		"""SCPI: CONFigure:MUTex:CATalog \n
		Snippet: value: CatalogStruct = driver.configure.mutex.get_catalog() \n
		No command help available \n
			:return: structure: for return value, see the help for CatalogStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:MUTex:CATalog?', self.__class__.CatalogStruct())

	def clone(self) -> 'Mutex':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mutex(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
