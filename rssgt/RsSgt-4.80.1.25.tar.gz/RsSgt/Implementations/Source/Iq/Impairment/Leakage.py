from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Leakage:
	"""Leakage commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("leakage", core, parent)

	def get_icomponent(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:LEAKage:I \n
		Snippet: value: float = driver.source.iq.impairment.leakage.get_icomponent() \n
		Sets the carrier leakage amplitude for the I-signal component. \n
			:return: ipart: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:IMPairment:LEAKage:I?')
		return Conversions.str_to_float(response)

	def set_icomponent(self, ipart: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:LEAKage:I \n
		Snippet: driver.source.iq.impairment.leakage.set_icomponent(ipart = 1.0) \n
		Sets the carrier leakage amplitude for the I-signal component. \n
			:param ipart: float Range: -10 to 10
		"""
		param = Conversions.decimal_value_to_str(ipart)
		self._core.io.write(f'SOURce<HwInstance>:IQ:IMPairment:LEAKage:I {param}')

	def get_qcomponent(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:LEAKage:Q \n
		Snippet: value: float = driver.source.iq.impairment.leakage.get_qcomponent() \n
		Sets the carrier leakage amplitude for the Q-signal component. \n
			:return: qpart: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:IMPairment:LEAKage:Q?')
		return Conversions.str_to_float(response)

	def set_qcomponent(self, qpart: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:LEAKage:Q \n
		Snippet: driver.source.iq.impairment.leakage.set_qcomponent(qpart = 1.0) \n
		Sets the carrier leakage amplitude for the Q-signal component. \n
			:param qpart: float Range: -10 to 10
		"""
		param = Conversions.decimal_value_to_str(qpart)
		self._core.io.write(f'SOURce<HwInstance>:IQ:IMPairment:LEAKage:Q {param}')
