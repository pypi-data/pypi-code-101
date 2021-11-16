'''_2559.py

ZerolBevelGearMeshSystemDeflection
'''


from mastapy.system_model.connections_and_sockets.gears import _2058
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6690
from mastapy.system_model.analyses_and_results.power_flows import _3880
from mastapy.gears.rating.zerol_bevel import _334
from mastapy.system_model.analyses_and_results.system_deflections import _2426
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ZerolBevelGearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshSystemDeflection',)


class ZerolBevelGearMeshSystemDeflection(_2426.BevelGearMeshSystemDeflection):
    '''ZerolBevelGearMeshSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2058.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2058.ZerolBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6690.ZerolBevelGearMeshLoadCase':
        '''ZerolBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6690.ZerolBevelGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3880.ZerolBevelGearMeshPowerFlow':
        '''ZerolBevelGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3880.ZerolBevelGearMeshPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def rating(self) -> '_334.ZerolBevelGearMeshRating':
        '''ZerolBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_334.ZerolBevelGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_334.ZerolBevelGearMeshRating':
        '''ZerolBevelGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_334.ZerolBevelGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
