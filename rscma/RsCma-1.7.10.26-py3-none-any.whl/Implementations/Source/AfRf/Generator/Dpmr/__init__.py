from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpmr:
	"""Dpmr commands group definition. 13 total commands, 1 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpmr", core, parent)

	@property
	def ccode(self):
		"""ccode commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ccode'):
			from .Ccode import Ccode
			self._ccode = Ccode(self._core, self._cmd_group)
		return self._ccode

	# noinspection PyTypeChecker
	def get_pattern(self) -> enums.NxdnPatternB:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:PATTern \n
		Snippet: value: enums.NxdnPatternB = driver.source.afRf.generator.dpmr.get_pattern() \n
		No command help available \n
			:return: pattern: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:DPMR:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.NxdnPatternB)

	def set_pattern(self, pattern: enums.NxdnPatternB) -> None:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:PATTern \n
		Snippet: driver.source.afRf.generator.dpmr.set_pattern(pattern = enums.NxdnPatternB.CUST) \n
		No command help available \n
			:param pattern: No help available
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.NxdnPatternB)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:DPMR:PATTern {param}')

	def get_svalue(self) -> str:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:SVALue \n
		Snippet: value: str = driver.source.afRf.generator.dpmr.get_svalue() \n
		No command help available \n
			:return: svalue: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:DPMR:SVALue?')
		return trim_str_response(response)

	def set_svalue(self, svalue: str) -> None:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:SVALue \n
		Snippet: driver.source.afRf.generator.dpmr.set_svalue(svalue = r1) \n
		No command help available \n
			:param svalue: No help available
		"""
		param = Conversions.value_to_str(svalue)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:DPMR:SVALue {param}')

	def get_sid(self) -> str:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:SID \n
		Snippet: value: str = driver.source.afRf.generator.dpmr.get_sid() \n
		No command help available \n
			:return: sid: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:DPMR:SID?')
		return trim_str_response(response)

	def set_sid(self, sid: str) -> None:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:SID \n
		Snippet: driver.source.afRf.generator.dpmr.set_sid(sid = '1') \n
		No command help available \n
			:param sid: No help available
		"""
		param = Conversions.value_to_quoted_str(sid)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:DPMR:SID {param}')

	def get_did(self) -> str:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:DID \n
		Snippet: value: str = driver.source.afRf.generator.dpmr.get_did() \n
		No command help available \n
			:return: did: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:DPMR:DID?')
		return trim_str_response(response)

	def set_did(self, did: str) -> None:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:DID \n
		Snippet: driver.source.afRf.generator.dpmr.set_did(did = '1') \n
		No command help available \n
			:param did: No help available
		"""
		param = Conversions.value_to_quoted_str(did)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:DPMR:DID {param}')

	def get_pt_peer(self) -> bool:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:PTPeer \n
		Snippet: value: bool = driver.source.afRf.generator.dpmr.get_pt_peer() \n
		No command help available \n
			:return: emergency: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:DPMR:PTPeer?')
		return Conversions.str_to_bool(response)

	def set_pt_peer(self, emergency: bool) -> None:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:PTPeer \n
		Snippet: driver.source.afRf.generator.dpmr.set_pt_peer(emergency = False) \n
		No command help available \n
			:param emergency: No help available
		"""
		param = Conversions.bool_to_str(emergency)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:DPMR:PTPeer {param}')

	def get_emergency(self) -> bool:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:EMERgency \n
		Snippet: value: bool = driver.source.afRf.generator.dpmr.get_emergency() \n
		No command help available \n
			:return: emergency: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:DPMR:EMERgency?')
		return Conversions.str_to_bool(response)

	def set_emergency(self, emergency: bool) -> None:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:EMERgency \n
		Snippet: driver.source.afRf.generator.dpmr.set_emergency(emergency = False) \n
		No command help available \n
			:param emergency: No help available
		"""
		param = Conversions.bool_to_str(emergency)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:DPMR:EMERgency {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FskMode:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:MODE \n
		Snippet: value: enums.FskMode = driver.source.afRf.generator.dpmr.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DPMR:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FskMode)

	def get_standard_dev(self) -> List[float]:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:SDEViation \n
		Snippet: value: List[float] = driver.source.afRf.generator.dpmr.get_standard_dev() \n
		No command help available \n
			:return: sdeviation: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list_with_opc('SOURce:AFRF:GENerator<Instance>:DPMR:SDEViation?')
		return response

	def get_symbol_rate(self) -> float:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:SRATe \n
		Snippet: value: float = driver.source.afRf.generator.dpmr.get_symbol_rate() \n
		No command help available \n
			:return: srate: No help available
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DPMR:SRATe?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_filter_py(self) -> enums.PulseShapingFilter:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:FILTer \n
		Snippet: value: enums.PulseShapingFilter = driver.source.afRf.generator.dpmr.get_filter_py() \n
		No command help available \n
			:return: filter_py: No help available
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DPMR:FILTer?')
		return Conversions.str_to_scalar_enum(response, enums.PulseShapingFilter)

	def get_ro_factor(self) -> float:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:DPMR:ROFactor \n
		Snippet: value: float = driver.source.afRf.generator.dpmr.get_ro_factor() \n
		No command help available \n
			:return: ro_factor: No help available
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DPMR:ROFactor?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Dpmr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpmr(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
