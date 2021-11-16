from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def get_correction_table(self) -> str:
		"""SCPI: CATalog:SYSTem:ATTenuation:CTABle \n
		Snippet: value: str = driver.catalog.system.attenuation.get_correction_table() \n
		No command help available \n
			:return: name: No help available
		"""
		response = self._core.io.query_str('CATalog:SYSTem:ATTenuation:CTABle?')
		return trim_str_response(response)
