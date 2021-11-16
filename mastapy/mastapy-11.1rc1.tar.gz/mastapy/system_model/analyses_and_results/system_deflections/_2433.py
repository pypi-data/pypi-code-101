'''_2433.py

ClutchSystemDeflection
'''


from mastapy.system_model.analyses_and_results.system_deflections import _2431, _2451
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2303
from mastapy.system_model.analyses_and_results.static_loads import _6534
from mastapy.system_model.analyses_and_results.power_flows import _3773
from mastapy._internal.python_net import python_net_import

_CLUTCH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ClutchSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchSystemDeflection',)


class ClutchSystemDeflection(_2451.CouplingSystemDeflection):
    '''ClutchSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_connection(self) -> '_2431.ClutchConnectionSystemDeflection':
        '''ClutchConnectionSystemDeflection: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2431.ClutchConnectionSystemDeflection)(self.wrapped.ClutchConnection) if self.wrapped.ClutchConnection is not None else None

    @property
    def assembly_design(self) -> '_2303.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2303.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6534.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6534.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3773.ClutchPowerFlow':
        '''ClutchPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3773.ClutchPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
