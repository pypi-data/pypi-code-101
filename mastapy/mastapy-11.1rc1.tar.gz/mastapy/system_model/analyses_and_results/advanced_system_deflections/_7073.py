'''_7073.py

ShaftAdvancedSystemDeflection
'''


from typing import List

from mastapy.shafts import _19
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2208
from mastapy.system_model.analyses_and_results.static_loads import _6653
from mastapy.system_model.analyses_and_results.system_deflections import _2524
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6973
from mastapy._internal.python_net import python_net_import

_SHAFT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ShaftAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftAdvancedSystemDeflection',)


class ShaftAdvancedSystemDeflection(_6973.AbstractShaftAdvancedSystemDeflection):
    '''ShaftAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SHAFT_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self) -> '_19.ShaftDamageResults':
        '''ShaftDamageResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_19.ShaftDamageResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def component_design(self) -> '_2208.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2208.Shaft)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6653.ShaftLoadCase':
        '''ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6653.ShaftLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def planetaries(self) -> 'List[ShaftAdvancedSystemDeflection]':
        '''List[ShaftAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftAdvancedSystemDeflection))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2524.ShaftSystemDeflection]':
        '''List[ShaftSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2524.ShaftSystemDeflection))
        return value
