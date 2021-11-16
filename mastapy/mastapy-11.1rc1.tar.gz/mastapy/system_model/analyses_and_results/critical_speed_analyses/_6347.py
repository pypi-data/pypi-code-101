'''_6347.py

SpringDamperConnectionCriticalSpeedAnalysis
'''


from mastapy.system_model.connections_and_sockets.couplings import _2077
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6660
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6280
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'SpringDamperConnectionCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionCriticalSpeedAnalysis',)


class SpringDamperConnectionCriticalSpeedAnalysis(_6280.CouplingConnectionCriticalSpeedAnalysis):
    '''SpringDamperConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_CONNECTION_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2077.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2077.SpringDamperConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6660.SpringDamperConnectionLoadCase':
        '''SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6660.SpringDamperConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
