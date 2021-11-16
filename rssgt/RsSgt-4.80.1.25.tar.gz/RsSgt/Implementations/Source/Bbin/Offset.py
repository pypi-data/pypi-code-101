from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def get_icomponent(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:OFFSet:I \n
		Snippet: value: float = driver.source.bbin.offset.get_icomponent() \n
		This command enters a DC offset to the I / Q component of the external baseband signal. \n
			:return: ipart: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:OFFSet:I?')
		return Conversions.str_to_float(response)

	def set_icomponent(self, ipart: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:OFFSet:I \n
		Snippet: driver.source.bbin.offset.set_icomponent(ipart = 1.0) \n
		This command enters a DC offset to the I / Q component of the external baseband signal. \n
			:param ipart: float Range: -10 to 10, Unit: %FS
		"""
		param = Conversions.decimal_value_to_str(ipart)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:OFFSet:I {param}')

	def get_qcomponent(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:OFFSet:Q \n
		Snippet: value: float = driver.source.bbin.offset.get_qcomponent() \n
		This command enters a DC offset to the I / Q component of the external baseband signal. \n
			:return: qpart: float Range: -10 to 10, Unit: %FS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:OFFSet:Q?')
		return Conversions.str_to_float(response)

	def set_qcomponent(self, qpart: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:OFFSet:Q \n
		Snippet: driver.source.bbin.offset.set_qcomponent(qpart = 1.0) \n
		This command enters a DC offset to the I / Q component of the external baseband signal. \n
			:param qpart: float Range: -10 to 10, Unit: %FS
		"""
		param = Conversions.decimal_value_to_str(qpart)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:OFFSet:Q {param}')
