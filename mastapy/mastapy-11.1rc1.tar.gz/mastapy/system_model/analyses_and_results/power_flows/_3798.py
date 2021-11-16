'''_3798.py

CylindricalGearMeshPowerFlow
'''


from mastapy.system_model.connections_and_sockets.gears import _2036
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6562
from mastapy.gears.rating.cylindrical import _420
from mastapy.system_model.analyses_and_results.power_flows import _3809
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CylindricalGearMeshPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshPowerFlow',)


class CylindricalGearMeshPowerFlow(_3809.GearMeshPowerFlow):
    '''CylindricalGearMeshPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_MESH_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2036.CylindricalGearMesh':
        '''CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2036.CylindricalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6562.CylindricalGearMeshLoadCase':
        '''CylindricalGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6562.CylindricalGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def rating(self) -> '_420.CylindricalGearMeshRating':
        '''CylindricalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_420.CylindricalGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_420.CylindricalGearMeshRating':
        '''CylindricalGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_420.CylindricalGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
