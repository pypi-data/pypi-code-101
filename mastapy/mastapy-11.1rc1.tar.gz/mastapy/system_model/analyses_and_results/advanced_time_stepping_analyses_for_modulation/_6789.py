'''_6789.py

MassDiscAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.part_model import _2188
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6623
from mastapy.system_model.analyses_and_results.system_deflections import _2499
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6836
from mastapy._internal.python_net import python_net_import

_MASS_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'MassDiscAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscAdvancedTimeSteppingAnalysisForModulation',)


class MassDiscAdvancedTimeSteppingAnalysisForModulation(_6836.VirtualComponentAdvancedTimeSteppingAnalysisForModulation):
    '''MassDiscAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2188.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2188.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6623.MassDiscLoadCase':
        '''MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6623.MassDiscLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2499.MassDiscSystemDeflection':
        '''MassDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2499.MassDiscSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def planetaries(self) -> 'List[MassDiscAdvancedTimeSteppingAnalysisForModulation]':
        '''List[MassDiscAdvancedTimeSteppingAnalysisForModulation]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscAdvancedTimeSteppingAnalysisForModulation))
        return value
