from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Train:
	"""Train commands group definition. 30 total commands, 5 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("train", core, parent)

	@property
	def dexchange(self):
		"""dexchange commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_dexchange'):
			from .Dexchange import Dexchange
			self._dexchange = Dexchange(self._core, self._cmd_group)
		return self._dexchange

	@property
	def hopping(self):
		"""hopping commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_hopping'):
			from .Hopping import Hopping
			self._hopping = Hopping(self._core, self._cmd_group)
		return self._hopping

	@property
	def offTime(self):
		"""offTime commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_offTime'):
			from .OffTime import OffTime
			self._offTime = OffTime(self._core, self._cmd_group)
		return self._offTime

	@property
	def ontime(self):
		"""ontime commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ontime'):
			from .Ontime import Ontime
			self._ontime = Ontime(self._core, self._cmd_group)
		return self._ontime

	@property
	def repetition(self):
		"""repetition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_repetition'):
			from .Repetition import Repetition
			self._repetition = Repetition(self._core, self._cmd_group)
		return self._repetition

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:PULM:TRAin:CATalog \n
		Snippet: value: List[str] = driver.source.pulm.train.get_catalog() \n
		Queries the available pulse train files in the specified directory. \n
			:return: catalog: string List of list filenames, separated by commas
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:TRAin:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:PULM:TRAin:DELete \n
		Snippet: driver.source.pulm.train.delete(filename = '1') \n
		Deletes the specified pulse train file. Refer to 'Accessing Files in the Default or in a Specified Directory' for general
		information on file handling in the default and in a specific directory. \n
			:param filename: string Filename or complete file path; file extension is optional.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:PULM:TRAin:DELete {param}')

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:PULM:TRAin:SELect \n
		Snippet: value: str = driver.source.pulm.train.get_select() \n
		Selects or creates a data list in pulse train mode. If the list with the selected name does not exist, a new list is
		created. \n
			:return: filename: string Filename or complete file path; file extension can be omitted.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:TRAin:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:PULM:TRAin:SELect \n
		Snippet: driver.source.pulm.train.set_select(filename = '1') \n
		Selects or creates a data list in pulse train mode. If the list with the selected name does not exist, a new list is
		created. \n
			:param filename: string Filename or complete file path; file extension can be omitted.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:PULM:TRAin:SELect {param}')

	def clone(self) -> 'Train':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Train(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
