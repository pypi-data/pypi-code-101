'''_5294.py

FaceGearSetCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2254
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5292, _5293, _5299
from mastapy.system_model.analyses_and_results.mbd_analyses import _5145
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'FaceGearSetCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundMultibodyDynamicsAnalysis',)


class FaceGearSetCompoundMultibodyDynamicsAnalysis(_5299.GearSetCompoundMultibodyDynamicsAnalysis):
    '''FaceGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundMultibodyDynamicsAnalysis.TYPE'):
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
    def face_gears_compound_multibody_dynamics_analysis(self) -> 'List[_5292.FaceGearCompoundMultibodyDynamicsAnalysis]':
        '''List[FaceGearCompoundMultibodyDynamicsAnalysis]: 'FaceGearsCompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsCompoundMultibodyDynamicsAnalysis, constructor.new(_5292.FaceGearCompoundMultibodyDynamicsAnalysis))
        return value

    @property
    def face_meshes_compound_multibody_dynamics_analysis(self) -> 'List[_5293.FaceGearMeshCompoundMultibodyDynamicsAnalysis]':
        '''List[FaceGearMeshCompoundMultibodyDynamicsAnalysis]: 'FaceMeshesCompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesCompoundMultibodyDynamicsAnalysis, constructor.new(_5293.FaceGearMeshCompoundMultibodyDynamicsAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5145.FaceGearSetMultibodyDynamicsAnalysis]':
        '''List[FaceGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5145.FaceGearSetMultibodyDynamicsAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5145.FaceGearSetMultibodyDynamicsAnalysis]':
        '''List[FaceGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5145.FaceGearSetMultibodyDynamicsAnalysis))
        return value
