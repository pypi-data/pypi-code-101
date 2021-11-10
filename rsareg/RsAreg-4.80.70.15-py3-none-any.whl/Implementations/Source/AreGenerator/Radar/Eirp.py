from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eirp:
	"""Eirp commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eirp", core, parent)

	# noinspection PyTypeChecker
	def get_sensor(self) -> enums.AregPowSens:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:EIRP:SENSor \n
		Snippet: value: enums.AregPowSens = driver.source.areGenerator.radar.eirp.get_sensor() \n
		Queries if and which sensor is used to measure the EIRP value. \n
			:return: areg_pow_sen_selec: SEN4| SEN3| SEN2| SEN1| UDEFined UDEFined No sensor is selected for EIRP measurement. However, there can be power sensors connected to one of the 'USB' connectors or the 'Sensor' connector of the R&S AREG100A. Sent the method RsAreg.Slist.listPy query to find out if and which power sensors are connected to the instrument. SEN4|SEN3|SEN2|SEN1 Indicates that a power sensor is connected to the frontend. The number SENx indicates the subsequent number in the sensor mapping list of the corresponding sensor. Observe the most left column in the 'NRP Sensor Mapping' dialog. See method RsAreg.Slist.Element.Mapping.set.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:EIRP:SENSor?')
		return Conversions.str_to_scalar_enum(response, enums.AregPowSens)

	def set_sensor(self, areg_pow_sen_selec: enums.AregPowSens) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:EIRP:SENSor \n
		Snippet: driver.source.areGenerator.radar.eirp.set_sensor(areg_pow_sen_selec = enums.AregPowSens.SEN1) \n
		Queries if and which sensor is used to measure the EIRP value. \n
			:param areg_pow_sen_selec: SEN4| SEN3| SEN2| SEN1| UDEFined UDEFined No sensor is selected for EIRP measurement. However, there can be power sensors connected to one of the 'USB' connectors or the 'Sensor' connector of the R&S AREG100A. Sent the method RsAreg.Slist.listPy query to find out if and which power sensors are connected to the instrument. SEN4|SEN3|SEN2|SEN1 Indicates that a power sensor is connected to the frontend. The number SENx indicates the subsequent number in the sensor mapping list of the corresponding sensor. Observe the most left column in the 'NRP Sensor Mapping' dialog. See method RsAreg.Slist.Element.Mapping.set.
		"""
		param = Conversions.enum_scalar_to_str(areg_pow_sen_selec, enums.AregPowSens)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:RADar:EIRP:SENSor {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:EIRP \n
		Snippet: value: float = driver.source.areGenerator.radar.eirp.get_value() \n
		Queries the measured EIRP value of the radar sensor. For details, see 'EIRP calculation'. \n
			:return: areg_radar_eirp: float Range: -150 to 150
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:EIRP?')
		return Conversions.str_to_float(response)
