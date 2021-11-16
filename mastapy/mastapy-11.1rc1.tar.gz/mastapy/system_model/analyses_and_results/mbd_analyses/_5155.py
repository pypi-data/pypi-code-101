'''_5155.py

HypoidGearSetMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2260
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6609
from mastapy.system_model.analyses_and_results.mbd_analyses import _5154, _5153, _5093
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'HypoidGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetMultibodyDynamicsAnalysis',)


class HypoidGearSetMultibodyDynamicsAnalysis(_5093.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis):
    '''HypoidGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2260.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2260.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6609.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6609.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def gears(self) -> 'List[_5154.HypoidGearMultibodyDynamicsAnalysis]':
        '''List[HypoidGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Gears, constructor.new(_5154.HypoidGearMultibodyDynamicsAnalysis))
        return value

    @property
    def hypoid_gears_multibody_dynamics_analysis(self) -> 'List[_5154.HypoidGearMultibodyDynamicsAnalysis]':
        '''List[HypoidGearMultibodyDynamicsAnalysis]: 'HypoidGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsMultibodyDynamicsAnalysis, constructor.new(_5154.HypoidGearMultibodyDynamicsAnalysis))
        return value

    @property
    def hypoid_meshes_multibody_dynamics_analysis(self) -> 'List[_5153.HypoidGearMeshMultibodyDynamicsAnalysis]':
        '''List[HypoidGearMeshMultibodyDynamicsAnalysis]: 'HypoidMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesMultibodyDynamicsAnalysis, constructor.new(_5153.HypoidGearMeshMultibodyDynamicsAnalysis))
        return value
