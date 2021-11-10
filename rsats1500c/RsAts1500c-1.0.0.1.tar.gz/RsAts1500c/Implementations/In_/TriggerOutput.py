from ...Internal import Instrument


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TriggerOutput:
	"""Trigger output of the inner axis movement"""
	def __init__(self, io: Instrument):
		self._io = io

	def set_state(self, state: bool) -> None:
		"""CONT:IN:TRIG:STAT \n
		Enables or disables the generation of a hardware trigger event at every given number of degrees of inner axis movement.
		The number of degrees is specified in set_step()"""
		cmd = 'CONT:IN:TRIG:STAT ' + ('1' if state is True else '0')
		self._io.write(cmd)

	def set_step(self, step: float) -> None:
		"""CONT:IN:TRIG:STEP \n
		Configures the inner axis to generate a trigger event every given number of degrees, if enabled.
		The range of step sizes depends on several parameters, for example inner speed and measurement instrument speed. We recommend a minimum step size of 1° for 15°/s inner axis speed."""
		cmd = f'CONT:IN:TRIG:STEP {format(step, ".2f")}'
		self._io.write(cmd)
