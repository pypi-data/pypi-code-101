# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioskeleton.views.bone.BoneView`` class."""

from collections import namedtuple

from pyramid.httpexceptions import HTTPForbidden

from ....tests import DBUnitTestCase


# =============================================================================
class UViewsBoneBoneView(DBUnitTestCase):
    """Unit test class for testing
 :class:`modules.cioskeleton.views.bone.BoneView`."""

    # -------------------------------------------------------------------------
    def test_view(self):
        """[u:modules.cioskeleton.views.bone.BoneView.index]"""
        from ....tests import TEST_INI
        from ..views.bone import BoneView
        from .. import ModuleCioSkeleton

        # Inactive module
        self.request.matched_route = namedtuple('Route', 'name')(
            name='bone_index')
        self.assertRaises(HTTPForbidden, BoneView(self.request).index)

        # Active module
        self.request.registry['modules'] = {
            'chrysalio.modules.cioskeleton': ModuleCioSkeleton(TEST_INI)}
        self.request.registry['modules_off'] = set()
        self.assertFalse(BoneView(self.request).index())
