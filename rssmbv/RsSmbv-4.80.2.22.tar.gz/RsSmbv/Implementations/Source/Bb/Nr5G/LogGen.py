from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LogGen:
	"""LogGen commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logGen", core, parent)

	def get_output(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:LOGGen:OUTPut \n
		Snippet: value: str = driver.source.bb.nr5G.logGen.get_output() \n
		No command help available \n
			:return: log_gen_output_path: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:LOGGen:OUTPut?')
		return trim_str_response(response)

	def set_output(self, log_gen_output_path: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:LOGGen:OUTPut \n
		Snippet: driver.source.bb.nr5G.logGen.set_output(log_gen_output_path = '1') \n
		No command help available \n
			:param log_gen_output_path: No help available
		"""
		param = Conversions.value_to_quoted_str(log_gen_output_path)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:LOGGen:OUTPut {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:LOGGen:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.logGen.get_state() \n
		No command help available \n
			:return: log_gen_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:LOGGen:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, log_gen_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:LOGGen:STATe \n
		Snippet: driver.source.bb.nr5G.logGen.set_state(log_gen_state = False) \n
		No command help available \n
			:param log_gen_state: No help available
		"""
		param = Conversions.bool_to_str(log_gen_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:LOGGen:STATe {param}')
