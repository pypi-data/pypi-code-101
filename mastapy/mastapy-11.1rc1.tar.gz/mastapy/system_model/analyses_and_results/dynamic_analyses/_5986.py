'''_5986.py

BearingDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2167
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6519
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6014
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'BearingDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDynamicAnalysis',)


class BearingDynamicAnalysis(_6014.ConnectorDynamicAnalysis):
    '''BearingDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEARING_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2167.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2167.Bearing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6519.BearingLoadCase':
        '''BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6519.BearingLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def planetaries(self) -> 'List[BearingDynamicAnalysis]':
        '''List[BearingDynamicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(BearingDynamicAnalysis))
        return value
