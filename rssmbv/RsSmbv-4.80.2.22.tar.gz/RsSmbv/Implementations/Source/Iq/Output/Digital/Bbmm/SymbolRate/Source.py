from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.BboutClocSour, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:SRATe:SOURce \n
		Snippet: driver.source.iq.output.digital.bbmm.symbolRate.source.set(source = enums.BboutClocSour.DOUT, iqConnector = repcap.IqConnector.Default) \n
		No command help available \n
			:param source: No help available
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.BboutClocSour)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:SRATe:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, iqConnector=repcap.IqConnector.Default) -> enums.BboutClocSour:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:BBMM<CH>:SRATe:SOURce \n
		Snippet: value: enums.BboutClocSour = driver.source.iq.output.digital.bbmm.symbolRate.source.get(iqConnector = repcap.IqConnector.Default) \n
		No command help available \n
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: source: No help available"""
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce:IQ:OUTPut:DIGital:BBMM{iqConnector_cmd_val}:SRATe:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.BboutClocSour)
