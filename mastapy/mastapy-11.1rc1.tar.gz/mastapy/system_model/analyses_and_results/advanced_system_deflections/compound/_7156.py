'''_7156.py

CylindricalGearMeshCompoundAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2036
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7024
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7167
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'CylindricalGearMeshCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshCompoundAdvancedSystemDeflection',)


class CylindricalGearMeshCompoundAdvancedSystemDeflection(_7167.GearMeshCompoundAdvancedSystemDeflection):
    '''CylindricalGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2036.CylindricalGearMesh':
        '''CylindricalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2036.CylindricalGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2036.CylindricalGearMesh':
        '''CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2036.CylindricalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7024.CylindricalGearMeshAdvancedSystemDeflection]':
        '''List[CylindricalGearMeshAdvancedSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_7024.CylindricalGearMeshAdvancedSystemDeflection))
        return value

    @property
    def planetaries(self) -> 'List[CylindricalGearMeshCompoundAdvancedSystemDeflection]':
        '''List[CylindricalGearMeshCompoundAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(CylindricalGearMeshCompoundAdvancedSystemDeflection))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_7024.CylindricalGearMeshAdvancedSystemDeflection]':
        '''List[CylindricalGearMeshAdvancedSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_7024.CylindricalGearMeshAdvancedSystemDeflection))
        return value
