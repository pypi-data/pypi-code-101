# pylint: disable = import-outside-toplevel
"""Tests of ``initialize.Initialize`` class."""

from pkg_resources import register_loader_type, DefaultProvider
from _pytest.assertion.rewrite import AssertionRewritingHook

# pylint: disable = unused-import
from ..models.dbgroup import DBGroup  # noqa
# pylint: enable = unused-import
from . import DBUnitTestCase


# =============================================================================
class UInitializeInitialize(DBUnitTestCase):
    """Unit test class for :class:`initialize.Initialize`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        super(UInitializeInitialize, self).setUp()
        register_loader_type(AssertionRewritingHook, DefaultProvider)

    # -------------------------------------------------------------------------
    def test_complete(self):
        """[u:initialize.Initialize.complete]"""
        from os import makedirs
        from os.path import dirname
        from transaction import manager
        from . import TEST_INI, TEST1_INI, TEST_DIR
        from ..initialize import Initialize

        global_config = {'__file__': TEST1_INI, 'here': dirname(TEST1_INI)}
        self.configurator.get_settings()['temporary'] = TEST_DIR
        makedirs(TEST_DIR)

        self.assertRaises(
            SystemExit, Initialize(self.configurator).complete,
            global_config, 'chrysalio', 'ciopopulate')

        settings = self.configurator.get_settings()
        settings['site.uid'] = 'testchrysalio'
        self.assertRaises(
            SystemExit, Initialize(self.configurator).complete,
            global_config, 'chrysalio', 'ciopopulate')

        global_config = {'__file__': TEST_INI, 'here': dirname(TEST_INI)}
        self.configurator.get_settings()['temporary'] = TEST_DIR
        self.assertRaises(
            SystemExit, Initialize(self.configurator).complete,
            global_config, 'chrysalio', 'ciopopulate')

        manager.commit()
        settings['testing'] = 'true'
        Initialize(self.configurator).complete(
            global_config, 'chrysalio', 'ciopopulate')
        self.assertIn('themes', self.configurator.registry)
        self.assertEqual(self.configurator.registry['settings']['theme'], '')
        self.assertEqual(len(self.configurator.registry['themes']), 1)

    # -------------------------------------------------------------------------
    def test_add_static_views(self):
        """[u:initialize.Initialize.add_static_views]"""
        from ..initialize import Initialize
        from . import TEST_DIR

        url = '/chrysalio/test/'
        self.assertIsNone(
            self.configurator.introspector.get('static views', url))

        Initialize(self.configurator).add_static_views(
            'chrysalio', (('test', TEST_DIR),))
        self.assertIsNotNone(
            self.configurator.introspector.get('static views', url))
