'''_3613.py

ZerolBevelGearSetStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2279
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6691
from mastapy.system_model.analyses_and_results.stability_analyses import _3614, _3612, _3500
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ZerolBevelGearSetStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetStabilityAnalysis',)


class ZerolBevelGearSetStabilityAnalysis(_3500.BevelGearSetStabilityAnalysis):
    '''ZerolBevelGearSetStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2279.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2279.ZerolBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6691.ZerolBevelGearSetLoadCase':
        '''ZerolBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6691.ZerolBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def zerol_bevel_gears_stability_analysis(self) -> 'List[_3614.ZerolBevelGearStabilityAnalysis]':
        '''List[ZerolBevelGearStabilityAnalysis]: 'ZerolBevelGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsStabilityAnalysis, constructor.new(_3614.ZerolBevelGearStabilityAnalysis))
        return value

    @property
    def zerol_bevel_meshes_stability_analysis(self) -> 'List[_3612.ZerolBevelGearMeshStabilityAnalysis]':
        '''List[ZerolBevelGearMeshStabilityAnalysis]: 'ZerolBevelMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesStabilityAnalysis, constructor.new(_3612.ZerolBevelGearMeshStabilityAnalysis))
        return value
