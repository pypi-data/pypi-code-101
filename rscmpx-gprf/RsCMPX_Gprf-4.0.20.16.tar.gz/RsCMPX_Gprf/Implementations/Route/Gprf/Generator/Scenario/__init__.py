from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenario", core, parent)

	@property
	def salone(self):
		"""salone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_salone'):
			from .Salone import Salone
			self._salone = Salone(self._core, self._cmd_group)
		return self._salone

	@property
	def iqOut(self):
		"""iqOut commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOut'):
			from .IqOut import IqOut
			self._iqOut = IqOut(self._core, self._cmd_group)
		return self._iqOut

	# noinspection PyTypeChecker
	def get_value(self) -> enums.GenScenario:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario \n
		Snippet: value: enums.GenScenario = driver.route.gprf.generator.scenario.get_value() \n
		No command help available \n
			:return: scenario: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:GENerator<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.GenScenario)

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
