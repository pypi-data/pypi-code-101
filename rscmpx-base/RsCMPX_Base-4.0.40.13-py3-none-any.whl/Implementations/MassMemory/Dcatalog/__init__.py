from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dcatalog:
	"""Dcatalog commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcatalog", core, parent)

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	def get(self, path_name: str = None) -> List[str]:
		"""SCPI: MMEMory:DCATalog \n
		Snippet: value: List[str] = driver.massMemory.dcatalog.get(path_name = '1') \n
		Returns the subdirectories of the current or of a specified directory. \n
			:param path_name: If this parameter is omitted, the command queries the contents of the current directory (see method RsCMPX_Base.MassMemory.CurrentDirectory.set) . If the wildcards ? or * are used, only the subdirectories matching this pattern are returned.
			:return: file_entry: Comma-separated list of strings with subdirectory names, one string per name"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('path_name', path_name, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'MMEMory:DCATalog? {param}'.rstrip())
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Dcatalog':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dcatalog(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
