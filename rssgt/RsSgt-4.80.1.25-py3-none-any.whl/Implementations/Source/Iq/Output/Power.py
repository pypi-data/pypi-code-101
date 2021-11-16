from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	def get_via(self) -> enums.IqOutDispViaType:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:POWer:VIA \n
		Snippet: value: enums.IqOutDispViaType = driver.source.iq.output.power.get_via() \n
		No command help available \n
			:return: via: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:POWer:VIA?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutDispViaType)

	def set_via(self, via: enums.IqOutDispViaType) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:POWer:VIA \n
		Snippet: driver.source.iq.output.power.set_via(via = enums.IqOutDispViaType.LEVel) \n
		No command help available \n
			:param via: No help available
		"""
		param = Conversions.enum_scalar_to_str(via, enums.IqOutDispViaType)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:POWer:VIA {param}')
