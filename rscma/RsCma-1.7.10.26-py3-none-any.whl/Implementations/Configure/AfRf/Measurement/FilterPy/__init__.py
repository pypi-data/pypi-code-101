from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def notch(self):
		"""notch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_notch'):
			from .Notch import Notch
			self._notch = Notch(self._core, self._cmd_group)
		return self._notch

	def get_disable(self) -> bool:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:FILTer:DISable \n
		Snippet: value: bool = driver.configure.afRf.measurement.filterPy.get_disable() \n
		No command help available \n
			:return: disable: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:FILTer:DISable?')
		return Conversions.str_to_bool(response)

	def set_disable(self, disable: bool) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:FILTer:DISable \n
		Snippet: driver.configure.afRf.measurement.filterPy.set_disable(disable = False) \n
		No command help available \n
			:param disable: No help available
		"""
		param = Conversions.bool_to_str(disable)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:FILTer:DISable {param}')

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
