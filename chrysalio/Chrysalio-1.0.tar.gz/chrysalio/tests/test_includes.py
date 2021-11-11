# pylint: disable = import-outside-toplevel
"""Tests of ``includes`` classes and functions."""

from os.path import join, dirname

from . import DBUnitTestCase
# pylint: disable = unused-import
from ..includes.modules.models import DBModule  # noqa
# pylint: enable = unused-import


# =============================================================================
class UIncludesLoadIncludes(DBUnitTestCase):
    """Unit test class for :func:`includes.load_includes`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ..security import PRINCIPALS
        from . import DummyRootFactory

        super(UIncludesLoadIncludes, self).setUp()

        self.configurator.set_root_factory(DummyRootFactory)
        self.configurator.registry['principals'] = list(PRINCIPALS)

    # -------------------------------------------------------------------------
    def test_bad_include(self):
        """[u:includes.load_includes] bad include"""
        from ..includes import load_includes

        settings = self.configurator.get_settings()
        settings['chrysalio.includes'] = 'chrysalio.includes.foo'
        self.assertRaises(
            SystemExit, load_includes, self.configurator)

    # -------------------------------------------------------------------------
    def test_conflict(self):
        """[u:includes.load_includes] conflict"""
        from . import TEST_INI
        from ..includes import load_includes

        settings = self.configurator.get_settings()
        settings.update({
            '__file__': TEST_INI,
            'chrysalio.includes':
            'chrysalio.includes.modules, chrysalio.modules.cioskeleton, '
            'chrysalio.tests.modules.conflict'})
        self.assertRaises(
            SystemExit, load_includes, self.configurator)

    # -------------------------------------------------------------------------
    def test_bad_depencendies(self):
        """[u:includes.load_includes] bad dependencies"""
        from . import TEST_INI
        from ..includes import load_includes

        settings = self.configurator.get_settings()
        settings['__file__'] = TEST_INI
        settings['chrysalio.includes'] = \
            'chrysalio.includes.modules, chrysalio.modules.cioskeleton'
        self.assertRaises(
            SystemExit, load_includes, self.configurator)

    # -------------------------------------------------------------------------
    def test_ok(self):
        """[u:includes.load_includes] ok"""
        from . import TEST_INI
        from ..includes import load_includes
        from ..modules.cioskeleton import ModuleCioSkeleton

        settings = self.configurator.get_settings()
        settings.update({
            'chrysalio.includes':
            'chrysalio.includes.themes, chrysalio.includes.modules, '
            'chrysalio.modules.cioldap, chrysalio.modules.cioskeleton',
            'theme.roots': join(dirname(__file__), '..', 'Themes'),
            'theme.patterns': 'Default'})
        self.configurator.registry['themes'] = {
            'Default': {'name': {'en': 'Default'}}}
        self.configurator.registry['settings']['theme'] = 'Default'
        self.configurator.get_settings()['__file__'] = TEST_INI

        # One module not activated
        load_includes(self.configurator)
        self.assertIn('modules', self.configurator.registry)
        self.assertIn('modules_off', self.configurator.registry)
        self.assertIn(
            'chrysalio.modules.cioskeleton',
            self.configurator.registry['modules'])
        self.assertEqual(len(self.configurator.registry['modules']), 2)
        self.assertIsInstance(
            self.configurator.registry['modules'][
                'chrysalio.modules.cioskeleton'], ModuleCioSkeleton)
