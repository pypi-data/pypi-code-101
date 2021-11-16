'''_6808.py

RootAssemblyAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5837
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2200
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _2348, _6719
from mastapy.system_model.analyses_and_results.system_deflections import _2520
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyAdvancedTimeSteppingAnalysisForModulation',)


class RootAssemblyAdvancedTimeSteppingAnalysisForModulation(_6719.AssemblyAdvancedTimeSteppingAnalysisForModulation):
    '''RootAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def results(self) -> '_5837.RootAssemblyHarmonicAnalysisResultsPropertyAccessor':
        '''RootAssemblyHarmonicAnalysisResultsPropertyAccessor: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5837.RootAssemblyHarmonicAnalysisResultsPropertyAccessor)(self.wrapped.Results) if self.wrapped.Results is not None else None

    @property
    def assembly_design(self) -> '_2200.RootAssembly':
        '''RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2200.RootAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def advanced_time_stepping_analysis_for_modulation_inputs(self) -> '_2348.AdvancedTimeSteppingAnalysisForModulation':
        '''AdvancedTimeSteppingAnalysisForModulation: 'AdvancedTimeSteppingAnalysisForModulationInputs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2348.AdvancedTimeSteppingAnalysisForModulation)(self.wrapped.AdvancedTimeSteppingAnalysisForModulationInputs) if self.wrapped.AdvancedTimeSteppingAnalysisForModulationInputs is not None else None

    @property
    def system_deflection_results(self) -> '_2520.RootAssemblySystemDeflection':
        '''RootAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2520.RootAssemblySystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
