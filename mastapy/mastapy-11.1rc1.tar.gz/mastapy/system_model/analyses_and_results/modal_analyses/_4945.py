'''_4945.py

ZerolBevelGearSetModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2279
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6691
from mastapy.system_model.analyses_and_results.system_deflections import _2560
from mastapy.system_model.analyses_and_results.modal_analyses import _4944, _4943, _4823
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ZerolBevelGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetModalAnalysis',)


class ZerolBevelGearSetModalAnalysis(_4823.BevelGearSetModalAnalysis):
    '''ZerolBevelGearSetModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2560.ZerolBevelGearSetSystemDeflection':
        '''ZerolBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2560.ZerolBevelGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def zerol_bevel_gears_modal_analysis(self) -> 'List[_4944.ZerolBevelGearModalAnalysis]':
        '''List[ZerolBevelGearModalAnalysis]: 'ZerolBevelGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsModalAnalysis, constructor.new(_4944.ZerolBevelGearModalAnalysis))
        return value

    @property
    def zerol_bevel_meshes_modal_analysis(self) -> 'List[_4943.ZerolBevelGearMeshModalAnalysis]':
        '''List[ZerolBevelGearMeshModalAnalysis]: 'ZerolBevelMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesModalAnalysis, constructor.new(_4943.ZerolBevelGearMeshModalAnalysis))
        return value
