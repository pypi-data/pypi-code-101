from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	def get_source(self) -> List[str]:
		"""SCPI: DIAGnostic:TRIGger:NRMMw:MEASurement<Instance>:MEValuation:SOURce \n
		Snippet: value: List[str] = driver.diagnostic.trigger.nrMmw.measurement.multiEval.get_source() \n
		No command help available \n
			:return: trigger: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:TRIGger:NRMMw:MEASurement<Instance>:MEValuation:SOURce?')
		return Conversions.str_to_str_list(response)

	def set_source(self, trigger: List[str]) -> None:
		"""SCPI: DIAGnostic:TRIGger:NRMMw:MEASurement<Instance>:MEValuation:SOURce \n
		Snippet: driver.diagnostic.trigger.nrMmw.measurement.multiEval.set_source(trigger = ['1', '2', '3']) \n
		No command help available \n
			:param trigger: No help available
		"""
		param = Conversions.list_to_csv_quoted_str(trigger)
		self._core.io.write(f'DIAGnostic:TRIGger:NRMMw:MEASurement<Instance>:MEValuation:SOURce {param}')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
