'''_4010.py

ZerolBevelGearMeshCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2058
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3880
from mastapy.system_model.analyses_and_results.power_flows.compound import _3900
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ZerolBevelGearMeshCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshCompoundPowerFlow',)


class ZerolBevelGearMeshCompoundPowerFlow(_3900.BevelGearMeshCompoundPowerFlow):
    '''ZerolBevelGearMeshCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2058.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2058.ZerolBevelGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2058.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2058.ZerolBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3880.ZerolBevelGearMeshPowerFlow]':
        '''List[ZerolBevelGearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_3880.ZerolBevelGearMeshPowerFlow))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3880.ZerolBevelGearMeshPowerFlow]':
        '''List[ZerolBevelGearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_3880.ZerolBevelGearMeshPowerFlow))
        return value
