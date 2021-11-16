from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def snumber(self):
		"""snumber commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_snumber'):
			from .Snumber import Snumber
			self._snumber = Snumber(self._core, self._cmd_group)
		return self._snumber

	def get_debug(self) -> bool:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:DEBug \n
		Snippet: value: bool = driver.diagnostic.gprf.measurement.get_debug() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:DEBug?')
		return Conversions.str_to_bool(response)

	def set_debug(self, enable: bool) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:DEBug \n
		Snippet: driver.diagnostic.gprf.measurement.set_debug(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:DEBug {param}')

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
