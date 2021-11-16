'''_5100.py

BevelDifferentialGearMeshMultibodyDynamicsAnalysis
'''


from mastapy.system_model.connections_and_sockets.gears import _2028
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6523
from mastapy.system_model.analyses_and_results.mbd_analyses import _5105
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BevelDifferentialGearMeshMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMeshMultibodyDynamicsAnalysis',)


class BevelDifferentialGearMeshMultibodyDynamicsAnalysis(_5105.BevelGearMeshMultibodyDynamicsAnalysis):
    '''BevelDifferentialGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMeshMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2028.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2028.BevelDifferentialGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6523.BevelDifferentialGearMeshLoadCase':
        '''BevelDifferentialGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6523.BevelDifferentialGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
