from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sensor:
	"""Sensor commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sensor", core, parent)

	def get_aperture(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:SENSor:APERture \n
		Snippet: value: float = driver.source.power.servoing.sensor.get_aperture() \n
		Sets the aperture time (size of the acquisition interval) of the power sensor during power servoing. \n
			:return: aperture: float Range: 10e-6 to 100e-3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SERVoing:SENSor:APERture?')
		return Conversions.str_to_float(response)

	def set_aperture(self, aperture: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:SENSor:APERture \n
		Snippet: driver.source.power.servoing.sensor.set_aperture(aperture = 1.0) \n
		Sets the aperture time (size of the acquisition interval) of the power sensor during power servoing. \n
			:param aperture: float Range: 10e-6 to 100e-3
		"""
		param = Conversions.decimal_value_to_str(aperture)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SERVoing:SENSor:APERture {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.PowSensWithUndef:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:SENSor \n
		Snippet: value: enums.PowSensWithUndef = driver.source.power.servoing.sensor.get_value() \n
		Sets the power sensor as mapped with the remote command SLISt:ELEMent<ch>:MAPPing. \n
			:return: sensor: SENS1| SENS2| SENSor2| SENS3| SENSor3| SENS4| SENSor4| SENSor1| UNDefined
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SERVoing:SENSor?')
		return Conversions.str_to_scalar_enum(response, enums.PowSensWithUndef)

	def set_value(self, sensor: enums.PowSensWithUndef) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:SENSor \n
		Snippet: driver.source.power.servoing.sensor.set_value(sensor = enums.PowSensWithUndef.SENS1) \n
		Sets the power sensor as mapped with the remote command SLISt:ELEMent<ch>:MAPPing. \n
			:param sensor: SENS1| SENS2| SENSor2| SENS3| SENSor3| SENS4| SENSor4| SENSor1| UNDefined
		"""
		param = Conversions.enum_scalar_to_str(sensor, enums.PowSensWithUndef)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SERVoing:SENSor {param}')
