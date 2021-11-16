from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ddm:
	"""Ddm commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ddm", core, parent)

	def get_pct(self) -> float:
		"""SCPI: [SOURce<HW>]:ILS:[GS]:DDM:PCT \n
		Snippet: value: float = driver.source.ils.gs.ddm.get_pct() \n
		No command help available \n
			:return: pct: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:ILS:GS:DDM:PCT?')
		return Conversions.str_to_float(response)

	def set_pct(self, pct: float) -> None:
		"""SCPI: [SOURce<HW>]:ILS:[GS]:DDM:PCT \n
		Snippet: driver.source.ils.gs.ddm.set_pct(pct = 1.0) \n
		No command help available \n
			:param pct: No help available
		"""
		param = Conversions.decimal_value_to_str(pct)
		self._core.io.write(f'SOURce<HwInstance>:ILS:GS:DDM:PCT {param}')
