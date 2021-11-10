from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dbypass:
	"""Dbypass commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbypass", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:DBYPass:[STATe] \n
		Snippet: value: bool = driver.source.areGenerator.radar.dbypass.get_state() \n
		Enable to bypass the Doppler stage. For details, see 'Enable Doppler Bypass'. \n
			:return: areg_radar_dop_byp: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:DBYPass:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, areg_radar_dop_byp: bool) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:DBYPass:[STATe] \n
		Snippet: driver.source.areGenerator.radar.dbypass.set_state(areg_radar_dop_byp = False) \n
		Enable to bypass the Doppler stage. For details, see 'Enable Doppler Bypass'. \n
			:param areg_radar_dop_byp: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(areg_radar_dop_byp)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:RADar:DBYPass:STATe {param}')
