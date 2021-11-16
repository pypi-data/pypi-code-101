from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gdelay:
	"""Gdelay commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gdelay", core, parent)

	def get_cstate(self) -> bool:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:GDELay:CSTate \n
		Snippet: value: bool = driver.source.iq.output.digital.gdelay.get_cstate() \n
		Enables/disables group delay compensation. \n
			:return: comp_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce:IQ:OUTPut:DIGital:GDELay:CSTate?')
		return Conversions.str_to_bool(response)

	def set_cstate(self, comp_state: bool) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:GDELay:CSTate \n
		Snippet: driver.source.iq.output.digital.gdelay.set_cstate(comp_state = False) \n
		Enables/disables group delay compensation. \n
			:param comp_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(comp_state)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:GDELay:CSTate {param}')
