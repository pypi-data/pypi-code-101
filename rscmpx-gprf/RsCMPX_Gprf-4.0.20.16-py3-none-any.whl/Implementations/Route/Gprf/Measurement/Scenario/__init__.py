from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 6 total commands, 4 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenario", core, parent)

	@property
	def maProtocol(self):
		"""maProtocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maProtocol'):
			from .MaProtocol import MaProtocol
			self._maProtocol = MaProtocol(self._core, self._cmd_group)
		return self._maProtocol

	@property
	def salone(self):
		"""salone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_salone'):
			from .Salone import Salone
			self._salone = Salone(self._core, self._cmd_group)
		return self._salone

	@property
	def maiq(self):
		"""maiq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maiq'):
			from .Maiq import Maiq
			self._maiq = Maiq(self._core, self._cmd_group)
		return self._maiq

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	def get_cspath(self) -> str:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: value: str = driver.route.gprf.measurement.scenario.get_cspath() \n
		No command help available \n
			:return: master: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath?')
		return trim_str_response(response)

	def set_cspath(self, master: str) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: driver.route.gprf.measurement.scenario.set_cspath(master = '1') \n
		No command help available \n
			:param master: No help available
		"""
		param = Conversions.value_to_quoted_str(master)
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.MeasScenario:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario \n
		Snippet: value: enums.MeasScenario = driver.route.gprf.measurement.scenario.get_value() \n
		No command help available \n
			:return: scenario: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.MeasScenario)

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
