from ...Internal import Instrument


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TriggerOutput:
	"""Trigger output of the outer axix movement"""
	def __init__(self, io: Instrument):
		self._io = io

	def set_state(self, state: bool) -> None:
		"""CONT:OUT:TRIG:STAT \n
		Enables or disables the generation of a hardware trigger event at every given number of degrees of outer axis movement.
		The number of degrees is specified in set_step()"""
		cmd = 'CONT:OUT:TRIG:STAT ' + ('1' if state is True else '0')
		self._io.write(cmd)

	def set_step(self, step: float) -> None:
		"""CONT:OUT:TRIG:STEP \n
		Configures the outer axis to generate a trigger event every given number of degrees, if enabled.
		The range of step sizes depends on several parameters, for example outer speed and measurement instrument speed. We recommend a minimum step size of 5° for 50°/s outer speed."""
		cmd = f'CONT:OUT:TRIG:STEP {format(step, ".2f")}'
		self._io.write(cmd)
