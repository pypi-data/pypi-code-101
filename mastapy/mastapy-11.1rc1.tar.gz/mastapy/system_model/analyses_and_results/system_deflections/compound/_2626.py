'''_2626.py

FaceGearMeshCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2038
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2474
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2631
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'FaceGearMeshCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshCompoundSystemDeflection',)


class FaceGearMeshCompoundSystemDeflection(_2631.GearMeshCompoundSystemDeflection):
    '''FaceGearMeshCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshCompoundSystemDeflection.TYPE'):
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
    def connection_analysis_cases_ready(self) -> 'List[_2474.FaceGearMeshSystemDeflection]':
        '''List[FaceGearMeshSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_2474.FaceGearMeshSystemDeflection))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2474.FaceGearMeshSystemDeflection]':
        '''List[FaceGearMeshSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_2474.FaceGearMeshSystemDeflection))
        return value
