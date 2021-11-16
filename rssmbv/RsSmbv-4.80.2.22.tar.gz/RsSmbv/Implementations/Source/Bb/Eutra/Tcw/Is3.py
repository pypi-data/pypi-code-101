from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Is3:
	"""Is3 commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("is3", core, parent)

	def get_ort_cover(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS3:ORTCover \n
		Snippet: value: int = driver.source.bb.eutra.tcw.is3.get_ort_cover() \n
		No command help available \n
			:return: ortho_cover: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS3:ORTCover?')
		return Conversions.str_to_int(response)

	def get_plevel(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS3:PLEVel \n
		Snippet: value: str = driver.source.bb.eutra.tcw.is3.get_plevel() \n
		Queries the power level of the interfering signal. \n
			:return: power_level: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS3:PLEVel?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_pr_condition(self) -> enums.EutraTcwPropagCond:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:IS3:PRCOndition \n
		Snippet: value: enums.EutraTcwPropagCond = driver.source.bb.eutra.tcw.is3.get_pr_condition() \n
		No command help available \n
			:return: propagation_condition: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TCW:IS3:PRCOndition?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTcwPropagCond)
