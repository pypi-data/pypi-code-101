'''_2431.py

ClutchConnectionSystemDeflection
'''


from mastapy.system_model.connections_and_sockets.couplings import _2069
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6532
from mastapy.system_model.analyses_and_results.power_flows import _3771
from mastapy.system_model.analyses_and_results.system_deflections import _2449
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ClutchConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionSystemDeflection',)


class ClutchConnectionSystemDeflection(_2449.CouplingConnectionSystemDeflection):
    '''ClutchConnectionSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_CONNECTION_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2069.ClutchConnection':
        '''ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2069.ClutchConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6532.ClutchConnectionLoadCase':
        '''ClutchConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6532.ClutchConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3771.ClutchConnectionPowerFlow':
        '''ClutchConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3771.ClutchConnectionPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
