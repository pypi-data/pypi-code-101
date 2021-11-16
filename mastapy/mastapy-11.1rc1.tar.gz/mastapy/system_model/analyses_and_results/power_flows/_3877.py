'''_3877.py

WormGearMeshPowerFlow
'''


from mastapy.system_model.connections_and_sockets.gears import _2056
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6687
from mastapy.gears.rating.worm import _338
from mastapy.system_model.analyses_and_results.power_flows import _3809
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'WormGearMeshPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshPowerFlow',)


class WormGearMeshPowerFlow(_3809.GearMeshPowerFlow):
    '''WormGearMeshPowerFlow

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_MESH_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2056.WormGearMesh':
        '''WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.WormGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6687.WormGearMeshLoadCase':
        '''WormGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6687.WormGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def rating(self) -> '_338.WormGearMeshRating':
        '''WormGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_338.WormGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_338.WormGearMeshRating':
        '''WormGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_338.WormGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
