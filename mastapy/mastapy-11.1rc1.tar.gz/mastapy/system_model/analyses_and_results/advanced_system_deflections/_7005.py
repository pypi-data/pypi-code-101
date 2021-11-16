'''_7005.py

ConceptGearMeshAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2032
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6541
from mastapy.gears.rating.concept import _504
from mastapy.system_model.analyses_and_results.system_deflections import _2440
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7036
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ConceptGearMeshAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshAdvancedSystemDeflection',)


class ConceptGearMeshAdvancedSystemDeflection(_7036.GearMeshAdvancedSystemDeflection):
    '''ConceptGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2032.ConceptGearMesh':
        '''ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2032.ConceptGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6541.ConceptGearMeshLoadCase':
        '''ConceptGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6541.ConceptGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def component_detailed_analysis(self) -> '_504.ConceptGearMeshRating':
        '''ConceptGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_504.ConceptGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2440.ConceptGearMeshSystemDeflection]':
        '''List[ConceptGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2440.ConceptGearMeshSystemDeflection))
        return value
