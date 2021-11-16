from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	# noinspection PyTypeChecker
	def get_vehicle(self) -> enums.RefVehicle:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:REFerence:VEHicle \n
		Snippet: value: enums.RefVehicle = driver.source.bb.gnss.sv.selection.reference.get_vehicle() \n
		No command help available \n
			:return: reference_vehicle: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:SELection:REFerence:VEHicle?')
		return Conversions.str_to_scalar_enum(response, enums.RefVehicle)

	def set_vehicle(self, reference_vehicle: enums.RefVehicle) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:REFerence:VEHicle \n
		Snippet: driver.source.bb.gnss.sv.selection.reference.set_vehicle(reference_vehicle = enums.RefVehicle.V1) \n
		No command help available \n
			:param reference_vehicle: No help available
		"""
		param = Conversions.enum_scalar_to_str(reference_vehicle, enums.RefVehicle)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:SELection:REFerence:VEHicle {param}')
