from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iq:
	"""Iq commands group definition. 153 total commands, 5 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def doherty(self):
		"""doherty commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_doherty'):
			from .Doherty import Doherty
			self._doherty = Doherty(self._core, self._cmd_group)
		return self._doherty

	@property
	def dpd(self):
		"""dpd commands group. 9 Sub-classes, 5 commands."""
		if not hasattr(self, '_dpd'):
			from .Dpd import Dpd
			self._dpd = Dpd(self._core, self._cmd_group)
		return self._dpd

	@property
	def impairment(self):
		"""impairment commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_impairment'):
			from .Impairment import Impairment
			self._impairment = Impairment(self._core, self._cmd_group)
		return self._impairment

	@property
	def output(self):
		"""output commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def swap(self):
		"""swap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_swap'):
			from .Swap import Swap
			self._swap = Swap(self._core, self._cmd_group)
		return self._swap

	def get_crest_factor(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:CREStfactor \n
		Snippet: value: float = driver.source.iq.get_crest_factor() \n
		Sets the crest factor of the IQ modulation signal. \n
			:return: crest_factor: float Range: 0 to 80
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:CREStfactor?')
		return Conversions.str_to_float(response)

	def set_crest_factor(self, crest_factor: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:CREStfactor \n
		Snippet: driver.source.iq.set_crest_factor(crest_factor = 1.0) \n
		Sets the crest factor of the IQ modulation signal. \n
			:param crest_factor: float Range: 0 to 80
		"""
		param = Conversions.decimal_value_to_str(crest_factor)
		self._core.io.write(f'SOURce<HwInstance>:IQ:CREStfactor {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.IqMode:
		"""SCPI: [SOURce<HW>]:IQ:SOURce \n
		Snippet: value: enums.IqMode = driver.source.iq.get_source() \n
		Sets the input signal for the I/Q modulator. \n
			:return: source: ANALog| BASeband
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.IqMode)

	def set_source(self, source: enums.IqMode) -> None:
		"""SCPI: [SOURce<HW>]:IQ:SOURce \n
		Snippet: driver.source.iq.set_source(source = enums.IqMode.ANALog) \n
		Sets the input signal for the I/Q modulator. \n
			:param source: ANALog| BASeband
		"""
		param = Conversions.enum_scalar_to_str(source, enums.IqMode)
		self._core.io.write(f'SOURce<HwInstance>:IQ:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:STATe \n
		Snippet: value: bool = driver.source.iq.get_state() \n
		Switches the I/Q modulation on and off. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:STATe \n
		Snippet: driver.source.iq.set_state(state = False) \n
		Switches the I/Q modulation on and off. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:STATe {param}')

	def get_wb_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:WBSTate \n
		Snippet: value: bool = driver.source.iq.get_wb_state() \n
		Selects optimized settings for wideband modulation signals. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:WBSTate?')
		return Conversions.str_to_bool(response)

	def set_wb_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:WBSTate \n
		Snippet: driver.source.iq.set_wb_state(state = False) \n
		Selects optimized settings for wideband modulation signals. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:WBSTate {param}')

	def clone(self) -> 'Iq':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
