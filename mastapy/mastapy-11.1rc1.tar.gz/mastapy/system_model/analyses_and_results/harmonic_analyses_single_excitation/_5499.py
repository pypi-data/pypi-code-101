'''_5499.py

StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2273
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6668
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5497, _5498, _5406
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'StraightBevelGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetHarmonicAnalysisOfSingleExcitation',)


class StraightBevelGearSetHarmonicAnalysisOfSingleExcitation(_5406.BevelGearSetHarmonicAnalysisOfSingleExcitation):
    '''StraightBevelGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2273.StraightBevelGearSet':
        '''StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2273.StraightBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6668.StraightBevelGearSetLoadCase':
        '''StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6668.StraightBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def straight_bevel_gears_harmonic_analysis_of_single_excitation(self) -> 'List[_5497.StraightBevelGearHarmonicAnalysisOfSingleExcitation]':
        '''List[StraightBevelGearHarmonicAnalysisOfSingleExcitation]: 'StraightBevelGearsHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearsHarmonicAnalysisOfSingleExcitation, constructor.new(_5497.StraightBevelGearHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def straight_bevel_meshes_harmonic_analysis_of_single_excitation(self) -> 'List[_5498.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation]':
        '''List[StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation]: 'StraightBevelMeshesHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelMeshesHarmonicAnalysisOfSingleExcitation, constructor.new(_5498.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation))
        return value
