from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Leakage:
	"""Leakage commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("leakage", core, parent)

	def get_icomponent(self) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:DIGital:LEAKage:I \n
		Snippet: value: float = driver.source.bb.impairment.digital.leakage.get_icomponent() \n
		Determines the leakage amplitude of the I or Q signal component of the corresponding stream \n
			:return: ipart: No help available
		"""
		response = self._core.io.query_str('SOURce:BB:IMPairment:DIGital:LEAKage:I?')
		return Conversions.str_to_float(response)

	def set_icomponent(self, ipart: float) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:DIGital:LEAKage:I \n
		Snippet: driver.source.bb.impairment.digital.leakage.set_icomponent(ipart = 1.0) \n
		Determines the leakage amplitude of the I or Q signal component of the corresponding stream \n
			:param ipart: float Range: -10 to 10
		"""
		param = Conversions.decimal_value_to_str(ipart)
		self._core.io.write(f'SOURce:BB:IMPairment:DIGital:LEAKage:I {param}')

	def get_qcomponent(self) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:DIGital:LEAKage:Q \n
		Snippet: value: float = driver.source.bb.impairment.digital.leakage.get_qcomponent() \n
		Determines the leakage amplitude of the I or Q signal component of the corresponding stream \n
			:return: qpart: No help available
		"""
		response = self._core.io.query_str('SOURce:BB:IMPairment:DIGital:LEAKage:Q?')
		return Conversions.str_to_float(response)

	def set_qcomponent(self, qpart: float) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:DIGital:LEAKage:Q \n
		Snippet: driver.source.bb.impairment.digital.leakage.set_qcomponent(qpart = 1.0) \n
		Determines the leakage amplitude of the I or Q signal component of the corresponding stream \n
			:param qpart: float Range: -10 to 10
		"""
		param = Conversions.decimal_value_to_str(qpart)
		self._core.io.write(f'SOURce:BB:IMPairment:DIGital:LEAKage:Q {param}')
