'''_6818.py

SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model.couplings import _2326
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6661
from mastapy.system_model.analyses_and_results.system_deflections import _2531
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6752
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation',)


class SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation(_6752.CouplingHalfAdvancedTimeSteppingAnalysisForModulation):
    '''SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2326.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2326.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6661.SpringDamperHalfLoadCase':
        '''SpringDamperHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6661.SpringDamperHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2531.SpringDamperHalfSystemDeflection':
        '''SpringDamperHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2531.SpringDamperHalfSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
