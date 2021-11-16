from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def get_step(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:PHASe:STEP \n
		Snippet: value: float = driver.source.bb.arbitrary.mcarrier.edit.carrier.phase.get_step() \n
		The command sets the step width by which the start phases of the carriers in the defined carrier range will be
		incremented. The phase settings are only valid if optimization of the crest factor is disabled
		(SOURce:BB:ARB:MCARrier:CFACtor:MODE OFF) . \n
			:return: step: float Range: -359.99 to 359.99, Unit: DEG
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:PHASe:STEP?')
		return Conversions.str_to_float(response)

	def set_step(self, step: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:PHASe:STEP \n
		Snippet: driver.source.bb.arbitrary.mcarrier.edit.carrier.phase.set_step(step = 1.0) \n
		The command sets the step width by which the start phases of the carriers in the defined carrier range will be
		incremented. The phase settings are only valid if optimization of the crest factor is disabled
		(SOURce:BB:ARB:MCARrier:CFACtor:MODE OFF) . \n
			:param step: float Range: -359.99 to 359.99, Unit: DEG
		"""
		param = Conversions.decimal_value_to_str(step)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:PHASe:STEP {param}')

	def get_start(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:PHASe:[STARt] \n
		Snippet: value: float = driver.source.bb.arbitrary.mcarrier.edit.carrier.phase.get_start() \n
		The command sets the start phase for the individual carriers in the defined carrier range.
		If the command BB:ARB:MCAR:EDIT:CARR:PHAS:STEP is used to define a step width, the phase entered here applies only to the
		starting carrier. The phases of the remaining carriers are stepped up or down by the phase value specified in the
		BB:ARB:MCAR:EDIT:CARR:PHAS:STEP command. The phase settings are only valid if optimization of the crest factor is
		disabled (SOURce:BB:ARB:MCARrier:CFACtor:MODE OFF) . \n
			:return: start: float Range: 0 to 359.99, Unit: DEG
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:PHASe:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, start: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:PHASe:[STARt] \n
		Snippet: driver.source.bb.arbitrary.mcarrier.edit.carrier.phase.set_start(start = 1.0) \n
		The command sets the start phase for the individual carriers in the defined carrier range.
		If the command BB:ARB:MCAR:EDIT:CARR:PHAS:STEP is used to define a step width, the phase entered here applies only to the
		starting carrier. The phases of the remaining carriers are stepped up or down by the phase value specified in the
		BB:ARB:MCAR:EDIT:CARR:PHAS:STEP command. The phase settings are only valid if optimization of the crest factor is
		disabled (SOURce:BB:ARB:MCARrier:CFACtor:MODE OFF) . \n
			:param start: float Range: 0 to 359.99, Unit: DEG
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:PHASe:STARt {param}')
