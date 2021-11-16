'''_6163.py

FaceGearSetCompoundDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2254
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6161, _6162, _6168
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6034
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'FaceGearSetCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundDynamicAnalysis',)


class FaceGearSetCompoundDynamicAnalysis(_6168.GearSetCompoundDynamicAnalysis):
    '''FaceGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2254.FaceGearSet':
        '''FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2254.FaceGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2254.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2254.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def face_gears_compound_dynamic_analysis(self) -> 'List[_6161.FaceGearCompoundDynamicAnalysis]':
        '''List[FaceGearCompoundDynamicAnalysis]: 'FaceGearsCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsCompoundDynamicAnalysis, constructor.new(_6161.FaceGearCompoundDynamicAnalysis))
        return value

    @property
    def face_meshes_compound_dynamic_analysis(self) -> 'List[_6162.FaceGearMeshCompoundDynamicAnalysis]':
        '''List[FaceGearMeshCompoundDynamicAnalysis]: 'FaceMeshesCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesCompoundDynamicAnalysis, constructor.new(_6162.FaceGearMeshCompoundDynamicAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6034.FaceGearSetDynamicAnalysis]':
        '''List[FaceGearSetDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_6034.FaceGearSetDynamicAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6034.FaceGearSetDynamicAnalysis]':
        '''List[FaceGearSetDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_6034.FaceGearSetDynamicAnalysis))
        return value
