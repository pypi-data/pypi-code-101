'''_2471.py

DatumSystemDeflection
'''


from mastapy.system_model.part_model import _2175
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6568
from mastapy.system_model.analyses_and_results.power_flows import _3802
from mastapy.system_model.analyses_and_results.system_deflections import _2435
from mastapy._internal.python_net import python_net_import

_DATUM_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'DatumSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumSystemDeflection',)


class DatumSystemDeflection(_2435.ComponentSystemDeflection):
    '''DatumSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _DATUM_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2175.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2175.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6568.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6568.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3802.DatumPowerFlow':
        '''DatumPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3802.DatumPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
