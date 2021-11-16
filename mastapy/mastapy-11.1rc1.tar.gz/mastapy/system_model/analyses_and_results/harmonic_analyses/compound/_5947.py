'''_5947.py

StraightBevelDiffGearSetCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2271
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5945, _5946, _5858
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'StraightBevelDiffGearSetCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundHarmonicAnalysis',)


class StraightBevelDiffGearSetCompoundHarmonicAnalysis(_5858.BevelGearSetCompoundHarmonicAnalysis):
    '''StraightBevelDiffGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2271.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2271.StraightBevelDiffGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2271.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2271.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def straight_bevel_diff_gears_compound_harmonic_analysis(self) -> 'List[_5945.StraightBevelDiffGearCompoundHarmonicAnalysis]':
        '''List[StraightBevelDiffGearCompoundHarmonicAnalysis]: 'StraightBevelDiffGearsCompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsCompoundHarmonicAnalysis, constructor.new(_5945.StraightBevelDiffGearCompoundHarmonicAnalysis))
        return value

    @property
    def straight_bevel_diff_meshes_compound_harmonic_analysis(self) -> 'List[_5946.StraightBevelDiffGearMeshCompoundHarmonicAnalysis]':
        '''List[StraightBevelDiffGearMeshCompoundHarmonicAnalysis]: 'StraightBevelDiffMeshesCompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesCompoundHarmonicAnalysis, constructor.new(_5946.StraightBevelDiffGearMeshCompoundHarmonicAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5782.StraightBevelDiffGearSetHarmonicAnalysis]':
        '''List[StraightBevelDiffGearSetHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5782.StraightBevelDiffGearSetHarmonicAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5782.StraightBevelDiffGearSetHarmonicAnalysis]':
        '''List[StraightBevelDiffGearSetHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5782.StraightBevelDiffGearSetHarmonicAnalysis))
        return value
