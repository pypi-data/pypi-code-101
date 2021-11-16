from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefLo:
	"""RefLo commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refLo", core, parent)

	# noinspection PyTypeChecker
	def get_output(self) -> enums.RefLoOutput:
		"""SCPI: CONNector:REFLo:OUTPut \n
		Snippet: value: enums.RefLoOutput = driver.connector.refLo.get_output() \n
		Determines the signal provided at the output connector [REF/LO OUT] (rear of the instrument) . \n
			:return: output: REF| LO| OFF
		"""
		response = self._core.io.query_str('CONNector:REFLo:OUTPut?')
		return Conversions.str_to_scalar_enum(response, enums.RefLoOutput)

	def set_output(self, output: enums.RefLoOutput) -> None:
		"""SCPI: CONNector:REFLo:OUTPut \n
		Snippet: driver.connector.refLo.set_output(output = enums.RefLoOutput.LO) \n
		Determines the signal provided at the output connector [REF/LO OUT] (rear of the instrument) . \n
			:param output: REF| LO| OFF
		"""
		param = Conversions.enum_scalar_to_str(output, enums.RefLoOutput)
		self._core.io.write(f'CONNector:REFLo:OUTPut {param}')
