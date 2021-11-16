'''_6734.py

ClutchAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model.couplings import _2303
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6534
from mastapy.system_model.analyses_and_results.system_deflections import _2433
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6750
from mastapy._internal.python_net import python_net_import

_CLUTCH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ClutchAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchAdvancedTimeSteppingAnalysisForModulation',)


class ClutchAdvancedTimeSteppingAnalysisForModulation(_6750.CouplingAdvancedTimeSteppingAnalysisForModulation):
    '''ClutchAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2303.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2303.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6534.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6534.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2433.ClutchSystemDeflection':
        '''ClutchSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2433.ClutchSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
