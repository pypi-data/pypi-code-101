from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	@property
	def rfOff(self):
		"""rfOff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfOff'):
			from .RfOff import RfOff
			self._rfOff = RfOff(self._core, self._cmd_group)
		return self._rfOff

	# noinspection PyTypeChecker
	def get_frequency(self) -> enums.RoscFreqExt:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:FREQuency \n
		Snippet: value: enums.RoscFreqExt = driver.source.roscillator.external.get_frequency() \n
		No command help available \n
			:return: frequency: No help available
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:EXTernal:FREQuency?')
		return Conversions.str_to_scalar_enum(response, enums.RoscFreqExt)

	def set_frequency(self, frequency: enums.RoscFreqExt) -> None:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:FREQuency \n
		Snippet: driver.source.roscillator.external.set_frequency(frequency = enums.RoscFreqExt._10MHZ) \n
		No command help available \n
			:param frequency: No help available
		"""
		param = Conversions.enum_scalar_to_str(frequency, enums.RoscFreqExt)
		self._core.io.write(f'SOURce:ROSCillator:EXTernal:FREQuency {param}')

	# noinspection PyTypeChecker
	def get_sbandwidth(self) -> enums.RoscBandWidtExt:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:SBANdwidth \n
		Snippet: value: enums.RoscBandWidtExt = driver.source.roscillator.external.get_sbandwidth() \n
		No command help available \n
			:return: sbandwidth: No help available
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:EXTernal:SBANdwidth?')
		return Conversions.str_to_scalar_enum(response, enums.RoscBandWidtExt)

	def set_sbandwidth(self, sbandwidth: enums.RoscBandWidtExt) -> None:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:SBANdwidth \n
		Snippet: driver.source.roscillator.external.set_sbandwidth(sbandwidth = enums.RoscBandWidtExt.NARRow) \n
		No command help available \n
			:param sbandwidth: No help available
		"""
		param = Conversions.enum_scalar_to_str(sbandwidth, enums.RoscBandWidtExt)
		self._core.io.write(f'SOURce:ROSCillator:EXTernal:SBANdwidth {param}')

	def clone(self) -> 'External':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = External(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
