from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, control: bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:STATe \n
		Snippet: driver.source.gprf.generator.state.set(control = False) \n
		Turns the generator on or off. \n
			:param control: Switch the generator ON or OFF.
		"""
		param = Conversions.bool_to_str(control)
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GeneratorState:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:STATe \n
		Snippet: value: enums.GeneratorState = driver.source.gprf.generator.state.get() \n
		Turns the generator on or off. \n
			:return: generator_state: OFF: generator switched off PEND: generator switched on but no signal available yet ON: generator switched on, signal available"""
		response = self._core.io.query_str_with_opc(f'SOURce:GPRF:GENerator<Instance>:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.GeneratorState)

	# noinspection PyTypeChecker
	def get_all(self) -> List[enums.GeneratorState]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:STATe:ALL \n
		Snippet: value: List[enums.GeneratorState] = driver.source.gprf.generator.state.get_all() \n
		No command help available \n
			:return: all_states: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:STATe:ALL?')
		return Conversions.str_to_list_enum(response, enums.GeneratorState)
