from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def get(self, xvalue: float, xunit: enums.Unknown) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:AMPM:VALue \n
		Snippet: value: float = driver.source.iq.doherty.amPm.value.get(xvalue = 1.0, xunit = enums.Unknown.DBM) \n
		No command help available \n
			:param xvalue: No help available
			:param xunit: No help available
			:return: delta_phase: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xvalue', xvalue, DataType.Float), ArgSingle('xunit', xunit, DataType.Enum, enums.Unknown))
		response = self._core.io.query_str(f'SOURce<HwInstance>:IQ:DOHerty:AMPM:VALue? {param}'.rstrip())
		return Conversions.str_to_float(response)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:AMPM:VALue:LEVel \n
		Snippet: value: float = driver.source.iq.doherty.amPm.value.get_level() \n
		No command help available \n
			:return: delta_phase: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:AMPM:VALue:LEVel?')
		return Conversions.str_to_float(response)

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:AMPM:VALue:PEP \n
		Snippet: value: float = driver.source.iq.doherty.amPm.value.get_pep() \n
		No command help available \n
			:return: delta_phase: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:AMPM:VALue:PEP?')
		return Conversions.str_to_float(response)
