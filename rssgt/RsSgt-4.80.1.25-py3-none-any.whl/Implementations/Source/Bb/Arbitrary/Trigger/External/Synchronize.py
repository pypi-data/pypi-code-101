from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Synchronize:
	"""Synchronize commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("synchronize", core, parent)

	def get_output(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:[EXTernal]:SYNChronize:OUTPut \n
		Snippet: value: bool = driver.source.bb.arbitrary.trigger.external.synchronize.get_output() \n
		(enabled for 'Trigger Source' External) Enables/disables output of the signal synchronous to the external trigger event. \n
			:return: output: 0| 1| OFF| ON ON The signal calculation starts simultaneously with the external trigger event but because of the instrument’s processing time the first samples are cut off and no signal is outputted. After elapsing of the internal processing time, the output signal is synchronous to the trigger event. OFF The signal output begins after elapsing of the processing time and starts with sample 0, i.e. the complete signal is outputted. This mode is recommended for triggering of short signal sequences with signal duration comparable with the processing time of the instrument.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:EXTernal:SYNChronize:OUTPut?')
		return Conversions.str_to_bool(response)

	def set_output(self, output: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:[EXTernal]:SYNChronize:OUTPut \n
		Snippet: driver.source.bb.arbitrary.trigger.external.synchronize.set_output(output = False) \n
		(enabled for 'Trigger Source' External) Enables/disables output of the signal synchronous to the external trigger event. \n
			:param output: 0| 1| OFF| ON ON The signal calculation starts simultaneously with the external trigger event but because of the instrument’s processing time the first samples are cut off and no signal is outputted. After elapsing of the internal processing time, the output signal is synchronous to the trigger event. OFF The signal output begins after elapsing of the processing time and starts with sample 0, i.e. the complete signal is outputted. This mode is recommended for triggering of short signal sequences with signal duration comparable with the processing time of the instrument.
		"""
		param = Conversions.bool_to_str(output)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:EXTernal:SYNChronize:OUTPut {param}')
