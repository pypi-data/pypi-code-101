'''_6858.py

BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6728
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _6854
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation',)


class BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation(_6854.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation):
    '''BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_6728.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation]':
        '''List[BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_6728.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6728.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation]':
        '''List[BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_6728.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation))
        return value
