'''_6809.py

ShaftAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.part_model.shaft_model import _2208
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6653
from mastapy.system_model.analyses_and_results.system_deflections import _2524
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6710
from mastapy._internal.python_net import python_net_import

_SHAFT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ShaftAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftAdvancedTimeSteppingAnalysisForModulation',)


class ShaftAdvancedTimeSteppingAnalysisForModulation(_6710.AbstractShaftAdvancedTimeSteppingAnalysisForModulation):
    '''ShaftAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _SHAFT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def system_deflection_results(self) -> '_2524.ShaftSystemDeflection':
        '''ShaftSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2524.ShaftSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def planetaries(self) -> 'List[ShaftAdvancedTimeSteppingAnalysisForModulation]':
        '''List[ShaftAdvancedTimeSteppingAnalysisForModulation]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftAdvancedTimeSteppingAnalysisForModulation))
        return value
