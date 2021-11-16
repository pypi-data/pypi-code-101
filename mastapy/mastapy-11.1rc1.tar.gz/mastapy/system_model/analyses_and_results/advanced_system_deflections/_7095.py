'''_7095.py

TorqueConverterAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2332
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6677
from mastapy.system_model.analyses_and_results.system_deflections import _2550
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7013
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'TorqueConverterAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterAdvancedSystemDeflection',)


class TorqueConverterAdvancedSystemDeflection(_7013.CouplingAdvancedSystemDeflection):
    '''TorqueConverterAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2332.TorqueConverter':
        '''TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2332.TorqueConverter)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6677.TorqueConverterLoadCase':
        '''TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6677.TorqueConverterLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2550.TorqueConverterSystemDeflection]':
        '''List[TorqueConverterSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2550.TorqueConverterSystemDeflection))
        return value
