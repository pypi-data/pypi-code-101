from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:[LEVel]:[IMMediate]:OFFSet \n
		Snippet: value: float = driver.source.power.level.immediate.get_offset() \n
		Specifies the constant level offset of a downstream attenuator/amplifier. If a level offset is entered, the level entered
		with POWer no longer corresponds to the RF output level. The following correlation applies: POWer = RF output level +
		POWer:OFFSet. Entering a level offset does not change the RF output level, but rather the query value of POWer. Only dB
		is permitted as the unit here. The linear units (V, W, etc.) are not permitted. \n
			:return: offset: float Range: -100 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:LEVel:IMMediate:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:[LEVel]:[IMMediate]:OFFSet \n
		Snippet: driver.source.power.level.immediate.set_offset(offset = 1.0) \n
		Specifies the constant level offset of a downstream attenuator/amplifier. If a level offset is entered, the level entered
		with POWer no longer corresponds to the RF output level. The following correlation applies: POWer = RF output level +
		POWer:OFFSet. Entering a level offset does not change the RF output level, but rather the query value of POWer. Only dB
		is permitted as the unit here. The linear units (V, W, etc.) are not permitted. \n
			:param offset: float Range: -100 to 100
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SOURce<HwInstance>:POWer:LEVel:IMMediate:OFFSet {param}')

	# noinspection PyTypeChecker
	def get_recall(self) -> enums.InclExcl:
		"""SCPI: [SOURce<HW>]:POWer:[LEVel]:[IMMediate]:RCL \n
		Snippet: value: enums.InclExcl = driver.source.power.level.immediate.get_recall() \n
		No command help available \n
			:return: rcl_excl_pow: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:LEVel:IMMediate:RCL?')
		return Conversions.str_to_scalar_enum(response, enums.InclExcl)

	def set_recall(self, rcl_excl_pow: enums.InclExcl) -> None:
		"""SCPI: [SOURce<HW>]:POWer:[LEVel]:[IMMediate]:RCL \n
		Snippet: driver.source.power.level.immediate.set_recall(rcl_excl_pow = enums.InclExcl.EXCLude) \n
		No command help available \n
			:param rcl_excl_pow: No help available
		"""
		param = Conversions.enum_scalar_to_str(rcl_excl_pow, enums.InclExcl)
		self._core.io.write(f'SOURce<HwInstance>:POWer:LEVel:IMMediate:RCL {param}')

	def get_amplitude(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:[LEVel]:[IMMediate]:[AMPLitude] \n
		Snippet: value: float = driver.source.power.level.immediate.get_amplitude() \n
		Sets the RF level at the RF output connector of the instrument. \n
			:return: amplitude: float Range: -120 to 25, Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:LEVel:IMMediate:AMPLitude?')
		return Conversions.str_to_float(response)

	def set_amplitude(self, amplitude: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:[LEVel]:[IMMediate]:[AMPLitude] \n
		Snippet: driver.source.power.level.immediate.set_amplitude(amplitude = 1.0) \n
		Sets the RF level at the RF output connector of the instrument. \n
			:param amplitude: float Range: -120 to 25, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(amplitude)
		self._core.io.write(f'SOURce<HwInstance>:POWer:LEVel:IMMediate:AMPLitude {param}')
