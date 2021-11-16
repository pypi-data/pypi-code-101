from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LfOutput:
	"""LfOutput commands group definition. 35 total commands, 8 Sub-groups, 3 group commands
	Repeated Capability: LfOutput, default value after init: LfOutput.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lfOutput", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_lfOutput_get', 'repcap_lfOutput_set', repcap.LfOutput.Nr1)

	def repcap_lfOutput_set(self, lfOutput: repcap.LfOutput) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to LfOutput.Default
		Default value after init: LfOutput.Nr1"""
		self._cmd_group.set_repcap_enum_value(lfOutput)

	def repcap_lfOutput_get(self) -> repcap.LfOutput:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def internal(self):
		"""internal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_internal'):
			from .Internal import Internal
			self._internal = Internal(self._core, self._cmd_group)
		return self._internal

	@property
	def period(self):
		"""period commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_period'):
			from .Period import Period
			self._period = Period(self._core, self._cmd_group)
		return self._period

	@property
	def shape(self):
		"""shape commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_shape'):
			from .Shape import Shape
			self._shape = Shape(self._core, self._cmd_group)
		return self._shape

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def sweep(self):
		"""sweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def get_offset(self) -> float:
		"""SCPI: [SOURce]:LFOutput:OFFSet \n
		Snippet: value: float = driver.source.lfOutput.get_offset() \n
		Sets a DC offset at the LF Output. \n
			:return: offset: float Range: depends on lfo voltage
		"""
		response = self._core.io.query_str('SOURce:LFOutput:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: [SOURce]:LFOutput:OFFSet \n
		Snippet: driver.source.lfOutput.set_offset(offset = 1.0) \n
		Sets a DC offset at the LF Output. \n
			:param offset: float Range: depends on lfo voltage
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SOURce:LFOutput:OFFSet {param}')

	# noinspection PyTypeChecker
	def get_simpedance(self) -> enums.LfSourceImp:
		"""SCPI: [SOURce]:LFOutput:SIMPedance \n
		Snippet: value: enums.LfSourceImp = driver.source.lfOutput.get_simpedance() \n
		Selects the impedance of the LF output. \n
			:return: simpedance: G600| G50
		"""
		response = self._core.io.query_str('SOURce:LFOutput:SIMPedance?')
		return Conversions.str_to_scalar_enum(response, enums.LfSourceImp)

	def set_simpedance(self, simpedance: enums.LfSourceImp) -> None:
		"""SCPI: [SOURce]:LFOutput:SIMPedance \n
		Snippet: driver.source.lfOutput.set_simpedance(simpedance = enums.LfSourceImp.G50) \n
		Selects the impedance of the LF output. \n
			:param simpedance: G600| G50
		"""
		param = Conversions.enum_scalar_to_str(simpedance, enums.LfSourceImp)
		self._core.io.write(f'SOURce:LFOutput:SIMPedance {param}')

	def get_voltage(self) -> float:
		"""SCPI: [SOURce]:LFOutput:VOLTage \n
		Snippet: value: float = driver.source.lfOutput.get_voltage() \n
		Sets the voltage of the LF output. \n
			:return: voltage: float Range: dynamic (see data sheet)
		"""
		response = self._core.io.query_str('SOURce:LFOutput:VOLTage?')
		return Conversions.str_to_float(response)

	def set_voltage(self, voltage: float) -> None:
		"""SCPI: [SOURce]:LFOutput:VOLTage \n
		Snippet: driver.source.lfOutput.set_voltage(voltage = 1.0) \n
		Sets the voltage of the LF output. \n
			:param voltage: float Range: dynamic (see data sheet)
		"""
		param = Conversions.decimal_value_to_str(voltage)
		self._core.io.write(f'SOURce:LFOutput:VOLTage {param}')

	def clone(self) -> 'LfOutput':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LfOutput(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
