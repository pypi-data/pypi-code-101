from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Custom:
	"""Custom commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("custom", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:ANTenna:CUSTom:[STATe] \n
		Snippet: value: bool = driver.source.areGenerator.radar.antenna.custom.get_state() \n
			INTRO_CMD_HELP: If enabled, you can use a custom antenna and define the transmitting and receiving gain values with the commands: \n
			- [:SOURce<hw>]:AREGenerator:RADar:ANTenna:REG:GAIN:TX
			- [:SOURce<hw>]:AREGenerator:RADar:ANTenna:REG:GAIN:RX. \n
			:return: areg_ant_cust_stat: 0| 1| OFF| ON 0 | OFF The predefined antenna gain settings for transmitting and receiving antenna are used. 1 | ON The customer-specific antenna gain settings for transmitting and receiving antenna apply.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:ANTenna:CUSTom:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, areg_ant_cust_stat: bool) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:ANTenna:CUSTom:[STATe] \n
		Snippet: driver.source.areGenerator.radar.antenna.custom.set_state(areg_ant_cust_stat = False) \n
			INTRO_CMD_HELP: If enabled, you can use a custom antenna and define the transmitting and receiving gain values with the commands: \n
			- [:SOURce<hw>]:AREGenerator:RADar:ANTenna:REG:GAIN:TX
			- [:SOURce<hw>]:AREGenerator:RADar:ANTenna:REG:GAIN:RX. \n
			:param areg_ant_cust_stat: 0| 1| OFF| ON 0 | OFF The predefined antenna gain settings for transmitting and receiving antenna are used. 1 | ON The customer-specific antenna gain settings for transmitting and receiving antenna apply.
		"""
		param = Conversions.bool_to_str(areg_ant_cust_stat)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:RADar:ANTenna:CUSTom:STATe {param}')
