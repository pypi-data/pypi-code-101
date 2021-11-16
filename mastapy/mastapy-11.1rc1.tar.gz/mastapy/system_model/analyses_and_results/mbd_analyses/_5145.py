'''_5145.py

FaceGearSetMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2254
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6586
from mastapy.system_model.analyses_and_results.mbd_analyses import _5144, _5143, _5151
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'FaceGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetMultibodyDynamicsAnalysis',)


class FaceGearSetMultibodyDynamicsAnalysis(_5151.GearSetMultibodyDynamicsAnalysis):
    '''FaceGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2254.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2254.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6586.FaceGearSetLoadCase':
        '''FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6586.FaceGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def gears(self) -> 'List[_5144.FaceGearMultibodyDynamicsAnalysis]':
        '''List[FaceGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Gears, constructor.new(_5144.FaceGearMultibodyDynamicsAnalysis))
        return value

    @property
    def face_gears_multibody_dynamics_analysis(self) -> 'List[_5144.FaceGearMultibodyDynamicsAnalysis]':
        '''List[FaceGearMultibodyDynamicsAnalysis]: 'FaceGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsMultibodyDynamicsAnalysis, constructor.new(_5144.FaceGearMultibodyDynamicsAnalysis))
        return value

    @property
    def face_meshes_multibody_dynamics_analysis(self) -> 'List[_5143.FaceGearMeshMultibodyDynamicsAnalysis]':
        '''List[FaceGearMeshMultibodyDynamicsAnalysis]: 'FaceMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesMultibodyDynamicsAnalysis, constructor.new(_5143.FaceGearMeshMultibodyDynamicsAnalysis))
        return value
