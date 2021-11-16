'''_5208.py

StraightBevelDiffGearSetMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2271
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6665
from mastapy.system_model.analyses_and_results.mbd_analyses import _5207, _5206, _5107
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'StraightBevelDiffGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetMultibodyDynamicsAnalysis',)


class StraightBevelDiffGearSetMultibodyDynamicsAnalysis(_5107.BevelGearSetMultibodyDynamicsAnalysis):
    '''StraightBevelDiffGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2271.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2271.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6665.StraightBevelDiffGearSetLoadCase':
        '''StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6665.StraightBevelDiffGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def gears(self) -> 'List[_5207.StraightBevelDiffGearMultibodyDynamicsAnalysis]':
        '''List[StraightBevelDiffGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Gears, constructor.new(_5207.StraightBevelDiffGearMultibodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_diff_gears_multibody_dynamics_analysis(self) -> 'List[_5207.StraightBevelDiffGearMultibodyDynamicsAnalysis]':
        '''List[StraightBevelDiffGearMultibodyDynamicsAnalysis]: 'StraightBevelDiffGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsMultibodyDynamicsAnalysis, constructor.new(_5207.StraightBevelDiffGearMultibodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_diff_meshes_multibody_dynamics_analysis(self) -> 'List[_5206.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis]':
        '''List[StraightBevelDiffGearMeshMultibodyDynamicsAnalysis]: 'StraightBevelDiffMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesMultibodyDynamicsAnalysis, constructor.new(_5206.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis))
        return value
