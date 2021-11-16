from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fixed:
	"""Fixed commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fixed", core, parent)

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	# noinspection PyTypeChecker
	def get_recall(self) -> enums.InclExcl:
		"""SCPI: [SOURce<HW>]:FREQuency:[FIXed]:RCL \n
		Snippet: value: enums.InclExcl = driver.source.frequency.fixed.get_recall() \n
		No command help available \n
			:return: rcl_excl_freq: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:FIXed:RCL?')
		return Conversions.str_to_scalar_enum(response, enums.InclExcl)

	def set_recall(self, rcl_excl_freq: enums.InclExcl) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:[FIXed]:RCL \n
		Snippet: driver.source.frequency.fixed.set_recall(rcl_excl_freq = enums.InclExcl.EXCLude) \n
		No command help available \n
			:param rcl_excl_freq: No help available
		"""
		param = Conversions.enum_scalar_to_str(rcl_excl_freq, enums.InclExcl)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:FIXed:RCL {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:[FIXed] \n
		Snippet: value: float = driver.source.frequency.fixed.get_value() \n
		Sets the RF frequency at the RF output connector of the selected instrument. Note: Enabled frequency offset affects the
		result of this query. The query returns the frequency, including frequency offset. \n
			:return: cw: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:FIXed?')
		return Conversions.str_to_float(response)

	def set_value(self, cw: float) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:[FIXed] \n
		Snippet: driver.source.frequency.fixed.set_value(cw = 1.0) \n
		Sets the RF frequency at the RF output connector of the selected instrument. Note: Enabled frequency offset affects the
		result of this query. The query returns the frequency, including frequency offset. \n
			:param cw: float
		"""
		param = Conversions.decimal_value_to_str(cw)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:FIXed {param}')

	def clone(self) -> 'Fixed':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fixed(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
