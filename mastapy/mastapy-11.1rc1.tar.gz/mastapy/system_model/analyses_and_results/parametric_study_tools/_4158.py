'''_4158.py

ZerolBevelGearSetParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2279
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6691
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4157, _4156, _4030
from mastapy.system_model.analyses_and_results.system_deflections import _2560
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ZerolBevelGearSetParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetParametricStudyTool',)


class ZerolBevelGearSetParametricStudyTool(_4030.BevelGearSetParametricStudyTool):
    '''ZerolBevelGearSetParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetParametricStudyTool.TYPE'):
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
    def zerol_bevel_gears_parametric_study_tool(self) -> 'List[_4157.ZerolBevelGearParametricStudyTool]':
        '''List[ZerolBevelGearParametricStudyTool]: 'ZerolBevelGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsParametricStudyTool, constructor.new(_4157.ZerolBevelGearParametricStudyTool))
        return value

    @property
    def zerol_bevel_meshes_parametric_study_tool(self) -> 'List[_4156.ZerolBevelGearMeshParametricStudyTool]':
        '''List[ZerolBevelGearMeshParametricStudyTool]: 'ZerolBevelMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesParametricStudyTool, constructor.new(_4156.ZerolBevelGearMeshParametricStudyTool))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2560.ZerolBevelGearSetSystemDeflection]':
        '''List[ZerolBevelGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2560.ZerolBevelGearSetSystemDeflection))
        return value
