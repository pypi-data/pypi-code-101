from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 9 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def cw(self):
		"""cw commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_cw'):
			from .Cw import Cw
			self._cw = Cw(self._core, self._cmd_group)
		return self._cw

	@property
	def fixed(self):
		"""fixed commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_fixed'):
			from .Fixed import Fixed
			self._fixed = Fixed(self._core, self._cmd_group)
		return self._fixed

	def get_offset(self) -> float:
		"""SCPI: [SOURce]:FREQuency:OFFSet \n
		Snippet: value: float = driver.source.frequency.get_offset() \n
		Sets a frequency offset, for example include the frequency shift of downstream instrument. Note: Enabled frequency offset
		affects the result of the query SOURce:FREQuency:CW? The query returns the frequency, including frequency offset. \n
			:return: offset: float Range: -3e9 to 3e9
		"""
		response = self._core.io.query_str('SOURce:FREQuency:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: [SOURce]:FREQuency:OFFSet \n
		Snippet: driver.source.frequency.set_offset(offset = 1.0) \n
		Sets a frequency offset, for example include the frequency shift of downstream instrument. Note: Enabled frequency offset
		affects the result of the query SOURce:FREQuency:CW? The query returns the frequency, including frequency offset. \n
			:param offset: float Range: -3e9 to 3e9
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SOURce:FREQuency:OFFSet {param}')

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
