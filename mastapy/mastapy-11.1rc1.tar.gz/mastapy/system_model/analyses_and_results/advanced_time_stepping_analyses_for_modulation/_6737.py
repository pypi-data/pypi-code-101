'''_6737.py

CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.connections_and_sockets import _1996
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.cycloidal import _2062
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6535, _6557
from mastapy.system_model.analyses_and_results.system_deflections import _2434, _2456
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6811
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation',)


class CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation(_6811.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation):
    '''CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _COAXIAL_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1996.CoaxialConnection':
        '''CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1996.CoaxialConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CoaxialConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectionDesign.__class__)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6535.CoaxialConnectionLoadCase':
        '''CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6535.CoaxialConnectionLoadCase.TYPE not in self.wrapped.ConnectionLoadCase.__class__.__mro__:
            raise CastException('Failed to cast connection_load_case to CoaxialConnectionLoadCase. Expected: {}.'.format(self.wrapped.ConnectionLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConnectionLoadCase.__class__)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2434.CoaxialConnectionSystemDeflection':
        '''CoaxialConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2434.CoaxialConnectionSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CoaxialConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
