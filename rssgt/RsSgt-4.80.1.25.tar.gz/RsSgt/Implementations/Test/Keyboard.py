from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Keyboard:
	"""Keyboard commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("keyboard", core, parent)

	def get_state(self) -> bool:
		"""SCPI: TEST:KEYBoard:[STATe] \n
		Snippet: value: bool = driver.test.keyboard.get_state() \n
		Enable/disable keyboard and LED test state. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('TEST:KEYBoard:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: TEST:KEYBoard:[STATe] \n
		Snippet: driver.test.keyboard.set_state(state = False) \n
		Enable/disable keyboard and LED test state. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TEST:KEYBoard:STATe {param}')
