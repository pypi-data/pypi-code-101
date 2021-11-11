from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Battery:
	"""Battery commands group definition. 26 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("battery", core, parent)

	@property
	def simulator(self):
		"""simulator commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_simulator'):
			from .Simulator import Simulator
			self._simulator = Simulator(self._core, self._cmd_group)
		return self._simulator

	@property
	def model(self):
		"""model commands group. 3 Sub-classes, 6 commands."""
		if not hasattr(self, '_model'):
			from .Model import Model
			self._model = Model(self._core, self._cmd_group)
		return self._model

	def get_status(self) -> str:
		"""SCPI: BATTery:STATus \n
		Snippet: value: str = driver.battery.get_status() \n
		Queries the status of the battery (idle, charging or discharging) . \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('BATTery:STATus?')
		return trim_str_response(response)
