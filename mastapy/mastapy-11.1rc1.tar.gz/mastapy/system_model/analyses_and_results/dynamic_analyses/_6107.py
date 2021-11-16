'''_6107.py

ZerolBevelGearSetDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2279
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6691
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6105, _6106, _5996
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ZerolBevelGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetDynamicAnalysis',)


class ZerolBevelGearSetDynamicAnalysis(_5996.BevelGearSetDynamicAnalysis):
    '''ZerolBevelGearSetDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetDynamicAnalysis.TYPE'):
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
    def zerol_bevel_gears_dynamic_analysis(self) -> 'List[_6105.ZerolBevelGearDynamicAnalysis]':
        '''List[ZerolBevelGearDynamicAnalysis]: 'ZerolBevelGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsDynamicAnalysis, constructor.new(_6105.ZerolBevelGearDynamicAnalysis))
        return value

    @property
    def zerol_bevel_meshes_dynamic_analysis(self) -> 'List[_6106.ZerolBevelGearMeshDynamicAnalysis]':
        '''List[ZerolBevelGearMeshDynamicAnalysis]: 'ZerolBevelMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesDynamicAnalysis, constructor.new(_6106.ZerolBevelGearMeshDynamicAnalysis))
        return value
