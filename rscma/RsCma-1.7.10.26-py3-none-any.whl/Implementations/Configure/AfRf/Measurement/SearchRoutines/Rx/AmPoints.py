from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmPoints:
	"""AmPoints commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amPoints", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:RX:AMPoints:ENABle \n
		Snippet: value: bool = driver.configure.afRf.measurement.searchRoutines.rx.amPoints.get_enable() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:RX:AMPoints:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:RX:AMPoints:ENABle \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.rx.amPoints.set_enable(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:RX:AMPoints:ENABle {param}')
