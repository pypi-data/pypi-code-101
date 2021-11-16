from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Afile:
	"""Afile commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("afile", core, parent)

	@property
	def separator(self):
		"""separator commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_separator'):
			from .Separator import Separator
			self._separator = Separator(self._core, self._cmd_group)
		return self._separator

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:AFILe:CATalog \n
		Snippet: value: List[str] = driver.source.correction.dexchange.afile.get_catalog() \n
		Requests a list of available ASCII files for export/import of user correction data. The individual files are separated by
		commas. The ASCII files are stored with the fixed file extensions *.txt or *.csv in a directory of the user's choice. The
		directory applicable to the commands is defined with the command method RsSgt.MassMemory.currentDirectory. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:DEXChange:AFILe:CATalog?')
		return Conversions.str_to_str_list(response)

	# noinspection PyTypeChecker
	def get_extension(self) -> enums.DexchExtension:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:AFILe:EXTension \n
		Snippet: value: enums.DexchExtension = driver.source.correction.dexchange.afile.get_extension() \n
		Selects the file extension of the ASCII file to be imported or exported. Selection TXT (text file) or CSV (Excel file) is
		available. \n
			:return: extension: TXT| CSV
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:DEXChange:AFILe:EXTension?')
		return Conversions.str_to_scalar_enum(response, enums.DexchExtension)

	def set_extension(self, extension: enums.DexchExtension) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:AFILe:EXTension \n
		Snippet: driver.source.correction.dexchange.afile.set_extension(extension = enums.DexchExtension.CSV) \n
		Selects the file extension of the ASCII file to be imported or exported. Selection TXT (text file) or CSV (Excel file) is
		available. \n
			:param extension: TXT| CSV
		"""
		param = Conversions.enum_scalar_to_str(extension, enums.DexchExtension)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:DEXChange:AFILe:EXTension {param}')

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:AFILe:SELect \n
		Snippet: value: str = driver.source.correction.dexchange.afile.get_select() \n
		Selects the ASCII file to be imported or exported. The ASCII files are stored with the fixed file extensions *.txt or *.
		csv in a directory of the user's choice. The directory applicable to the commands is defined with the command method
		RsSgt.MassMemory.currentDirectory. A path can also be specified in command SOUR:CORR:DEXC:AFIL:SEL, in which case the
		files are stored or loaded in the specified directory. \n
			:return: filename: ascii file name
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:DEXChange:AFILe:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:DEXChange:AFILe:SELect \n
		Snippet: driver.source.correction.dexchange.afile.set_select(filename = '1') \n
		Selects the ASCII file to be imported or exported. The ASCII files are stored with the fixed file extensions *.txt or *.
		csv in a directory of the user's choice. The directory applicable to the commands is defined with the command method
		RsSgt.MassMemory.currentDirectory. A path can also be specified in command SOUR:CORR:DEXC:AFIL:SEL, in which case the
		files are stored or loaded in the specified directory. \n
			:param filename: ascii file name
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:DEXChange:AFILe:SELect {param}')

	def clone(self) -> 'Afile':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Afile(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
