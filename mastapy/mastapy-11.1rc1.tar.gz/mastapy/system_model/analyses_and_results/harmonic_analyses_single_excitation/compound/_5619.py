'''_5619.py

SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2269
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _5617, _5618, _5536
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5490
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation',)


class SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(_5536.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation):
    '''SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2269.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2269.SpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2269.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2269.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def spiral_bevel_gears_compound_harmonic_analysis_of_single_excitation(self) -> 'List[_5617.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation]: 'SpiralBevelGearsCompoundHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCompoundHarmonicAnalysisOfSingleExcitation, constructor.new(_5617.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def spiral_bevel_meshes_compound_harmonic_analysis_of_single_excitation(self) -> 'List[_5618.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]: 'SpiralBevelMeshesCompoundHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCompoundHarmonicAnalysisOfSingleExcitation, constructor.new(_5618.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5490.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5490.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5490.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5490.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation))
        return value
