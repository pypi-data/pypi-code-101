'''_6120.py

BevelDifferentialGearMeshCompoundDynamicAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2028
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5990
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6125
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'BevelDifferentialGearMeshCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMeshCompoundDynamicAnalysis',)


class BevelDifferentialGearMeshCompoundDynamicAnalysis(_6125.BevelGearMeshCompoundDynamicAnalysis):
    '''BevelDifferentialGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMeshCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2028.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2028.BevelDifferentialGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2028.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2028.BevelDifferentialGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5990.BevelDifferentialGearMeshDynamicAnalysis]':
        '''List[BevelDifferentialGearMeshDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_5990.BevelDifferentialGearMeshDynamicAnalysis))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5990.BevelDifferentialGearMeshDynamicAnalysis]':
        '''List[BevelDifferentialGearMeshDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_5990.BevelDifferentialGearMeshDynamicAnalysis))
        return value
