'''_3937.py

FaceGearMeshCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2038
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3804
from mastapy.system_model.analyses_and_results.power_flows.compound import _3942
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'FaceGearMeshCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshCompoundPowerFlow',)


class FaceGearMeshCompoundPowerFlow(_3942.GearMeshCompoundPowerFlow):
    '''FaceGearMeshCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2038.FaceGearMesh':
        '''FaceGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2038.FaceGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2038.FaceGearMesh':
        '''FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2038.FaceGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3804.FaceGearMeshPowerFlow]':
        '''List[FaceGearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_3804.FaceGearMeshPowerFlow))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3804.FaceGearMeshPowerFlow]':
        '''List[FaceGearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_3804.FaceGearMeshPowerFlow))
        return value
