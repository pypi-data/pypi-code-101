from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Arb:
	"""Arb commands group definition. 12 total commands, 2 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("arb", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def samples(self):
		"""samples commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_samples'):
			from .Samples import Samples
			self._samples = Samples(self._core, self._cmd_group)
		return self._samples

	def get_crate(self) -> float:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:CRATe \n
		Snippet: value: float = driver.source.xrt.generator.arb.get_crate() \n
		No command help available \n
			:return: clock_rate: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:CRATe?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_crc_protect(self) -> enums.YesNoStatus:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:CRCProtect \n
		Snippet: value: enums.YesNoStatus = driver.source.xrt.generator.arb.get_crc_protect() \n
		No command help available \n
			:return: crc_protection: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:CRCProtect?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	def get_foffset(self) -> float:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:FOFFset \n
		Snippet: value: float = driver.source.xrt.generator.arb.get_foffset() \n
		No command help available \n
			:return: frequency_offset: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, frequency_offset: float) -> None:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:FOFFset \n
		Snippet: driver.source.xrt.generator.arb.set_foffset(frequency_offset = 1.0) \n
		No command help available \n
			:param frequency_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency_offset)
		self._core.io.write(f'SOURce:XRT:GENerator<Instance>:ARB:FOFFset {param}')

	def get_loffset(self) -> float:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:LOFFset \n
		Snippet: value: float = driver.source.xrt.generator.arb.get_loffset() \n
		No command help available \n
			:return: level_offset: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:LOFFset?')
		return Conversions.str_to_float(response)

	def get_poffset(self) -> float:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:POFFset \n
		Snippet: value: float = driver.source.xrt.generator.arb.get_poffset() \n
		No command help available \n
			:return: peak_offset: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:POFFset?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepeatMode:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:REPetition \n
		Snippet: value: enums.RepeatMode = driver.source.xrt.generator.arb.get_repetition() \n
		No command help available \n
			:return: repetition: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepeatMode)

	def set_repetition(self, repetition: enums.RepeatMode) -> None:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:REPetition \n
		Snippet: driver.source.xrt.generator.arb.set_repetition(repetition = enums.RepeatMode.CONTinuous) \n
		No command help available \n
			:param repetition: No help available
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepeatMode)
		self._core.io.write(f'SOURce:XRT:GENerator<Instance>:ARB:REPetition {param}')

	def clone(self) -> 'Arb':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Arb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
