'''_3984.py

SpiralBevelGearSetCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2269
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _3982, _3983, _3901
from mastapy.system_model.analyses_and_results.power_flows import _3854
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SpiralBevelGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundPowerFlow',)


class SpiralBevelGearSetCompoundPowerFlow(_3901.BevelGearSetCompoundPowerFlow):
    '''SpiralBevelGearSetCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2269.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2269.SpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2269.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2269.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def spiral_bevel_gears_compound_power_flow(self) -> 'List[_3982.SpiralBevelGearCompoundPowerFlow]':
        '''List[SpiralBevelGearCompoundPowerFlow]: 'SpiralBevelGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCompoundPowerFlow, constructor.new(_3982.SpiralBevelGearCompoundPowerFlow))
        return value

    @property
    def spiral_bevel_meshes_compound_power_flow(self) -> 'List[_3983.SpiralBevelGearMeshCompoundPowerFlow]':
        '''List[SpiralBevelGearMeshCompoundPowerFlow]: 'SpiralBevelMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCompoundPowerFlow, constructor.new(_3983.SpiralBevelGearMeshCompoundPowerFlow))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3854.SpiralBevelGearSetPowerFlow]':
        '''List[SpiralBevelGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3854.SpiralBevelGearSetPowerFlow))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3854.SpiralBevelGearSetPowerFlow]':
        '''List[SpiralBevelGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3854.SpiralBevelGearSetPowerFlow))
        return value
