# pylint: disable = import-outside-toplevel
"""Tests of ``includes.modules`` functions."""

from collections import OrderedDict

from transaction import manager

from ....tests import DBUnitTestCase
# pylint: disable = unused-import
from ....models.dbgroup import DBGroup  # noqa
# pylint: enable = unused-import


# =============================================================================
class UIncludesModulesIncludeme(DBUnitTestCase):
    """Unit test class for :func:`includes.modules.includeme`."""

    # -------------------------------------------------------------------------
    def test_configurator(self):
        """[u:includes.modules.includeme] with a configurator"""
        from ....menu import MENU_ADMIN
        from ....modes import MODE_HOME, MODE_ADMIN
        from ....tests import DummyRootFactory
        from .. import PRINCIPALS_MODULES, SUBMENU_MODULES, includeme
        from ..models import DBModule

        self.request.dbsession.add(
            DBModule(module_id='skeleton', inactive=True))
        manager.commit()
        self.configurator.set_root_factory(DummyRootFactory)
        self.configurator.registry['menu'] = [MENU_ADMIN]

        # With menu
        includeme(self.configurator)
        self.assertIn(
            PRINCIPALS_MODULES[0], self.configurator.registry['principals'])
        self.assertIn(
            SUBMENU_MODULES, self.configurator.registry['menu'][0][4])
        self.assertIn('modules', self.configurator.registry)
        self.assertIn('modules_off', self.configurator.registry)

        # With modes
        self.configurator.registry['modes'] = [MODE_HOME, MODE_ADMIN]
        includeme(self.configurator)
        mode = dict(self.configurator.registry['modes']).get('admin')
        self.assertIsNotNone(mode)
        self.assertEqual(mode[4][4][1], SUBMENU_MODULES)

        # pylint: disable = no-member
        DBModule.__table__.drop()
        # pylint: enable = no-member
        includeme(self.configurator)

    # -------------------------------------------------------------------------
    def test_dictionary(self):
        """[u:includes.modules.includeme] with a dictionary"""
        from .. import includeme

        module_set = set()
        includeme(module_set)
        self.assertNotIn('chrysalio.modules', module_set)

        module_dict = OrderedDict()
        includeme(module_dict)
        self.assertFalse(module_dict)
