'''_1793.py

LoadedToroidalRollerBearingRow
'''


from mastapy.bearings.bearing_results.rolling import _1792, _1764
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_LOADED_TOROIDAL_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedToroidalRollerBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedToroidalRollerBearingRow',)


class LoadedToroidalRollerBearingRow(_1764.LoadedRollerBearingRow):
    '''LoadedToroidalRollerBearingRow

    This is a mastapy class.
    '''

    TYPE = _LOADED_TOROIDAL_ROLLER_BEARING_ROW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedToroidalRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1792.LoadedToroidalRollerBearingResults':
        '''LoadedToroidalRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1792.LoadedToroidalRollerBearingResults)(self.wrapped.LoadedBearing) if self.wrapped.LoadedBearing is not None else None
