'''_5144.py

FaceGearMultibodyDynamicsAnalysis
'''


from mastapy.system_model.part_model.gears import _2253
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6584
from mastapy.system_model.analyses_and_results.mbd_analyses import _5150
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'FaceGearMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMultibodyDynamicsAnalysis',)


class FaceGearMultibodyDynamicsAnalysis(_5150.GearMultibodyDynamicsAnalysis):
    '''FaceGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2253.FaceGear':
        '''FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2253.FaceGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6584.FaceGearLoadCase':
        '''FaceGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6584.FaceGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
