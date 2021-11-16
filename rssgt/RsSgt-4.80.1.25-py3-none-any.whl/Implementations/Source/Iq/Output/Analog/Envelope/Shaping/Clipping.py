from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clipping:
	"""Clipping commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clipping", core, parent)

	def get_from_py(self) -> int:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:CLIPping:FROM \n
		Snippet: value: int = driver.source.iq.output.analog.envelope.shaping.clipping.get_from_py() \n
		Enables clipping and defines its limits. \n
			:return: clipping_from: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:CLIPping:FROM?')
		return Conversions.str_to_int(response)

	def set_from_py(self, clipping_from: int) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:CLIPping:FROM \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.clipping.set_from_py(clipping_from = 1) \n
		Enables clipping and defines its limits. \n
			:param clipping_from: integer Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(clipping_from)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:CLIPping:FROM {param}')

	def get_to(self) -> int:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:CLIPping:TO \n
		Snippet: value: int = driver.source.iq.output.analog.envelope.shaping.clipping.get_to() \n
		Enables clipping and defines its limits. \n
			:return: clipping_to: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:CLIPping:TO?')
		return Conversions.str_to_int(response)

	def set_to(self, clipping_to: int) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:CLIPping:TO \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.clipping.set_to(clipping_to = 1) \n
		Enables clipping and defines its limits. \n
			:param clipping_to: integer Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(clipping_to)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:CLIPping:TO {param}')
