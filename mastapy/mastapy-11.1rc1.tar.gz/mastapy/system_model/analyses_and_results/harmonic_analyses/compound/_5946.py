'''_5946.py

StraightBevelDiffGearMeshCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2052
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5781
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5857
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'StraightBevelDiffGearMeshCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshCompoundHarmonicAnalysis',)


class StraightBevelDiffGearMeshCompoundHarmonicAnalysis(_5857.BevelGearMeshCompoundHarmonicAnalysis):
    '''StraightBevelDiffGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2052.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2052.StraightBevelDiffGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2052.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2052.StraightBevelDiffGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5781.StraightBevelDiffGearMeshHarmonicAnalysis]':
        '''List[StraightBevelDiffGearMeshHarmonicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_5781.StraightBevelDiffGearMeshHarmonicAnalysis))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5781.StraightBevelDiffGearMeshHarmonicAnalysis]':
        '''List[StraightBevelDiffGearMeshHarmonicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_5781.StraightBevelDiffGearMeshHarmonicAnalysis))
        return value
