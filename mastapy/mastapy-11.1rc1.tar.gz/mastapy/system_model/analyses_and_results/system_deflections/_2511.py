'''_2511.py

PointLoadSystemDeflection
'''


from mastapy.system_model.part_model import _2197
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6641
from mastapy.system_model.analyses_and_results.power_flows import _3837
from mastapy.system_model.analyses_and_results.system_deflections import _2555
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'PointLoadSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadSystemDeflection',)


class PointLoadSystemDeflection(_2555.VirtualComponentSystemDeflection):
    '''PointLoadSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2197.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2197.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6641.PointLoadLoadCase':
        '''PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6641.PointLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3837.PointLoadPowerFlow':
        '''PointLoadPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3837.PointLoadPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
