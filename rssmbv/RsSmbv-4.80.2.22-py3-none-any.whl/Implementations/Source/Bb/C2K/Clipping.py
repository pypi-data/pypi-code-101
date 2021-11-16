from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clipping:
	"""Clipping commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clipping", core, parent)

	def get_level(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:CLIPping:LEVel \n
		Snippet: value: int = driver.source.bb.c2K.clipping.get_level() \n
		The command sets the limit for level clipping (Clipping) . This value indicates at what point the signal is clipped.
		It is specified as a percentage, relative to the highest level. 100% indicates that clipping does not take place. Level
		clipping is activated with the command BB:C2K:CLIPping:STATe \n
			:return: level: integer Range: 1 PCT to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:CLIPping:LEVel?')
		return Conversions.str_to_int(response)

	def set_level(self, level: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:CLIPping:LEVel \n
		Snippet: driver.source.bb.c2K.clipping.set_level(level = 1) \n
		The command sets the limit for level clipping (Clipping) . This value indicates at what point the signal is clipped.
		It is specified as a percentage, relative to the highest level. 100% indicates that clipping does not take place. Level
		clipping is activated with the command BB:C2K:CLIPping:STATe \n
			:param level: integer Range: 1 PCT to 100
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:CLIPping:LEVel {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Dimensions:
		"""SCPI: [SOURce<HW>]:BB:C2K:CLIPping:MODE \n
		Snippet: value: enums.Dimensions = driver.source.bb.c2K.clipping.get_mode() \n
		The command sets the method for level clipping (Clipping) . \n
			:return: mode: VECTor| SCALar VECTor The reference level is the amplitude | i+jq | SCALar The reference level is the absolute maximum of the I and Q values.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:CLIPping:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Dimensions)

	def set_mode(self, mode: enums.Dimensions) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:CLIPping:MODE \n
		Snippet: driver.source.bb.c2K.clipping.set_mode(mode = enums.Dimensions.SCALar) \n
		The command sets the method for level clipping (Clipping) . \n
			:param mode: VECTor| SCALar VECTor The reference level is the amplitude | i+jq | SCALar The reference level is the absolute maximum of the I and Q values.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Dimensions)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:CLIPping:MODE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:CLIPping:STATe \n
		Snippet: value: bool = driver.source.bb.c2K.clipping.get_state() \n
		The command activates level clipping (Clipping) . The value is defined with the command BB:C2K:CLIPping:LEVel, the mode
		of calculation with the command BB:C2K:CLIPping:MODE. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:CLIPping:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:CLIPping:STATe \n
		Snippet: driver.source.bb.c2K.clipping.set_state(state = False) \n
		The command activates level clipping (Clipping) . The value is defined with the command BB:C2K:CLIPping:LEVel, the mode
		of calculation with the command BB:C2K:CLIPping:MODE. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:CLIPping:STATe {param}')
