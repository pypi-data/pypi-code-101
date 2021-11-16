'''_6842.py

ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2279
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6691
from mastapy.system_model.analyses_and_results.system_deflections import _2560
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6840, _6841, _6731
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation',)


class ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation(_6731.BevelGearSetAdvancedTimeSteppingAnalysisForModulation):
    '''ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
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
    def zerol_bevel_gears_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_6840.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation]':
        '''List[ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation]: 'ZerolBevelGearsAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsAdvancedTimeSteppingAnalysisForModulation, constructor.new(_6840.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation))
        return value

    @property
    def zerol_bevel_meshes_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_6841.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        '''List[ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'ZerolBevelMeshesAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesAdvancedTimeSteppingAnalysisForModulation, constructor.new(_6841.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation))
        return value
