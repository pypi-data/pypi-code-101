from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modext:
	"""Modext commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modext", core, parent)

	# noinspection PyTypeChecker
	def get_impedance(self) -> enums.ImpG50G10K:
		"""SCPI: [SOURce]:INPut:MODext:IMPedance \n
		Snippet: value: enums.ImpG50G10K = driver.source.inputPy.modext.get_impedance() \n
		No command help available \n
			:return: impedance: No help available
		"""
		response = self._core.io.query_str('SOURce:INPut:MODext:IMPedance?')
		return Conversions.str_to_scalar_enum(response, enums.ImpG50G10K)

	def set_impedance(self, impedance: enums.ImpG50G10K) -> None:
		"""SCPI: [SOURce]:INPut:MODext:IMPedance \n
		Snippet: driver.source.inputPy.modext.set_impedance(impedance = enums.ImpG50G10K.G10K) \n
		No command help available \n
			:param impedance: No help available
		"""
		param = Conversions.enum_scalar_to_str(impedance, enums.ImpG50G10K)
		self._core.io.write(f'SOURce:INPut:MODext:IMPedance {param}')
