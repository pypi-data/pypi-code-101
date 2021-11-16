'''_2548.py

TorqueConverterConnectionSystemDeflection
'''


from mastapy.system_model.connections_and_sockets.couplings import _2079
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6676
from mastapy.system_model.analyses_and_results.power_flows import _3871
from mastapy.system_model.analyses_and_results.system_deflections import _2449
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'TorqueConverterConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionSystemDeflection',)


class TorqueConverterConnectionSystemDeflection(_2449.CouplingConnectionSystemDeflection):
    '''TorqueConverterConnectionSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_CONNECTION_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2079.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2079.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6676.TorqueConverterConnectionLoadCase':
        '''TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6676.TorqueConverterConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3871.TorqueConverterConnectionPowerFlow':
        '''TorqueConverterConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3871.TorqueConverterConnectionPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
