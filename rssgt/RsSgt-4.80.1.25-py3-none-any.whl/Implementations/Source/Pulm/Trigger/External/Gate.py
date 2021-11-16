from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gate:
	"""Gate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gate", core, parent)

	# noinspection PyTypeChecker
	def get_polarity(self) -> enums.NormalInverted:
		"""SCPI: [SOURce<HW>]:PULM:TRIGger:EXTernal:GATE:POLarity \n
		Snippet: value: enums.NormalInverted = driver.source.pulm.trigger.external.gate.get_polarity() \n
		Selects the polarity of the Gate signal. \n
			:return: polarity: NORMal| INVerted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:TRIGger:EXTernal:GATE:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.NormalInverted)

	def set_polarity(self, polarity: enums.NormalInverted) -> None:
		"""SCPI: [SOURce<HW>]:PULM:TRIGger:EXTernal:GATE:POLarity \n
		Snippet: driver.source.pulm.trigger.external.gate.set_polarity(polarity = enums.NormalInverted.INVerted) \n
		Selects the polarity of the Gate signal. \n
			:param polarity: NORMal| INVerted
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.NormalInverted)
		self._core.io.write(f'SOURce<HwInstance>:PULM:TRIGger:EXTernal:GATE:POLarity {param}')
