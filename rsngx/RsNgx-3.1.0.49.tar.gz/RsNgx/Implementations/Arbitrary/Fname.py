from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.Utilities import trim_str_response
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fname:
	"""Fname commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fname", core, parent)

	def set(self, filename: str, file_location: enums.Filename = None) -> None:
		"""SCPI: ARBitrary:FNAMe \n
		Snippet: driver.arbitrary.fname.set(filename = '1', file_location = enums.Filename.DEF) \n
		Sets or queries the file name and storage location for the QuickArb function. \n
			:param filename: Filename of the QuickArb function.
			:param file_location:
				- INT: Internal memory
				- EXT: USB stick
				- DEF: Internal memory"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('file_location', file_location, DataType.Enum, enums.Filename, is_optional=True))
		self._core.io.write(f'ARBitrary:FNAMe {param}'.rstrip())

	def get(self) -> str:
		"""SCPI: ARBitrary:FNAMe \n
		Snippet: value: str = driver.arbitrary.fname.get() \n
		Sets or queries the file name and storage location for the QuickArb function. \n
			:return: filename: Filename of the QuickArb function."""
		response = self._core.io.query_str(f'ARBitrary:FNAMe?')
		return trim_str_response(response)
