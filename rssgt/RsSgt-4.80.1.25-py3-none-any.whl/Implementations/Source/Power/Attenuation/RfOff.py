from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfOff:
	"""RfOff commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfOff", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PowRfOffMode:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:RFOFf:MODE \n
		Snippet: value: enums.PowRfOffMode = driver.source.power.attenuation.rfOff.get_mode() \n
		Determines the attenuator's state after the instrument is switched on. \n
			:return: mode: MAX| FATTenuated| FIXed| UNCHanged MAX = FATTenuated Sets attenuation to maximum when the RF signal is switched off. This setting is recommended for applications that require a high level of noise suppression. FIXed = UNCHanged Retains the current setting and keeps the output impedance constant during RF off.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ATTenuation:RFOFf:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PowRfOffMode)

	def set_mode(self, mode: enums.PowRfOffMode) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:RFOFf:MODE \n
		Snippet: driver.source.power.attenuation.rfOff.set_mode(mode = enums.PowRfOffMode.FIXed) \n
		Determines the attenuator's state after the instrument is switched on. \n
			:param mode: MAX| FATTenuated| FIXed| UNCHanged MAX = FATTenuated Sets attenuation to maximum when the RF signal is switched off. This setting is recommended for applications that require a high level of noise suppression. FIXed = UNCHanged Retains the current setting and keeps the output impedance constant during RF off.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PowRfOffMode)
		self._core.io.write(f'SOURce<HwInstance>:POWer:ATTenuation:RFOFf:MODE {param}')
