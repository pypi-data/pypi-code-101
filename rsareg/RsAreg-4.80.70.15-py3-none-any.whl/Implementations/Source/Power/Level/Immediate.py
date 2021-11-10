from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	# noinspection PyTypeChecker
	def get_recall(self) -> enums.InclExcl:
		"""SCPI: [SOURce<HW>]:POWer:[LEVel]:[IMMediate]:RCL \n
		Snippet: value: enums.InclExcl = driver.source.power.level.immediate.get_recall() \n
		No command help available \n
			:return: rcl: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:LEVel:IMMediate:RCL?')
		return Conversions.str_to_scalar_enum(response, enums.InclExcl)

	def set_recall(self, rcl: enums.InclExcl) -> None:
		"""SCPI: [SOURce<HW>]:POWer:[LEVel]:[IMMediate]:RCL \n
		Snippet: driver.source.power.level.immediate.set_recall(rcl = enums.InclExcl.EXCLude) \n
		No command help available \n
			:param rcl: No help available
		"""
		param = Conversions.enum_scalar_to_str(rcl, enums.InclExcl)
		self._core.io.write(f'SOURce<HwInstance>:POWer:LEVel:IMMediate:RCL {param}')
