from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MassMemory:
	"""MassMemory commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("massMemory", core, parent)

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	def get_hdd(self) -> bool:
		"""SCPI: SYSTem:MMEMory:HDD \n
		Snippet: value: bool = driver.system.massMemory.get_hdd() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SYSTem:MMEMory:HDD?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'MassMemory':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MassMemory(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
