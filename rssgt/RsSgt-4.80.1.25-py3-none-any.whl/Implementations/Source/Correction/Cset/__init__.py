from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cset:
	"""Cset commands group definition. 8 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cset", core, parent)

	@property
	def data(self):
		"""data commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce]:CORRection:CSET:CATalog \n
		Snippet: value: List[str] = driver.source.correction.cset.get_catalog() \n
		Requests a list of user correction tables. The individual lists are separated by commas. The lists are stored with the
		fixed file extensions *.uco in a directory of the user's choice. The directory applicable to the commands is defined with
		the command method RsSgt.MassMemory.currentDirectory. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce:CORRection:CSET:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce]:CORRection:CSET:DELete \n
		Snippet: driver.source.correction.cset.delete(filename = '1') \n
		Deletes the specified table. The lists are stored with the fixed file extensions *.uco in a directory of the user's
		choice. The directory applicable to the commands is defined with the command method RsSgt.MassMemory.currentDirectory. A
		path can also be specified in command SOUR:CORR:CSET:CAT?, in which case the file in the specified directory is deleted. \n
			:param filename: table name
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce:CORRection:CSET:DELete {param}')

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:[SELect] \n
		Snippet: value: str = driver.source.correction.cset.get_select() \n
		Selects or creates a file for the user correction data. If the file does not exist, the instrument automatically creates
		a new file with the name you assigned. Note the predefined file extensions under 'Extensions for User Files'.
		To determine the file location (directory/path) you can either enter it with the command directly, or use the command
		method RsSgt.MassMemory.currentDirectory.
		To activate level correction use the command [:​SOURce<hw>]:​CORRection[:​STATe]. \n
			:return: filename: table name
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:CSET:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:[SELect] \n
		Snippet: driver.source.correction.cset.set_select(filename = '1') \n
		Selects or creates a file for the user correction data. If the file does not exist, the instrument automatically creates
		a new file with the name you assigned. Note the predefined file extensions under 'Extensions for User Files'.
		To determine the file location (directory/path) you can either enter it with the command directly, or use the command
		method RsSgt.MassMemory.currentDirectory.
		To activate level correction use the command [:​SOURce<hw>]:​CORRection[:​STATe]. \n
			:param filename: table name
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:CSET:SELect {param}')

	def clone(self) -> 'Cset':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
