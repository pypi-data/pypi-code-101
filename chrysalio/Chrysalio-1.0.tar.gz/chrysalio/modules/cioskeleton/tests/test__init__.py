# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioskeleton`` classes and functions."""

from unittest import TestCase

from ....tests import ModuleTestCase


# =============================================================================
class UCioSkeletonIncludeme(ModuleTestCase):
    """Unit test class for :func:`modules.cioskeleton.includeme`."""

    # -------------------------------------------------------------------------
    def test_configurator(self):
        """[u:modules.cioskeleton.includeme] with a configurator"""
        from ....tests import TEST_INI
        from .. import includeme, ModuleCioSkeleton

        self.configurator.get_settings()['__file__'] = TEST_INI
        self.configurator.registry['themes'] = {
            '': {'path': None, 'name': {}, 'layout': 'layout.pt'}}

        includeme(self.configurator)
        self.assertTrue(self.configurator.registry['modules'])
        self.assertIn(
            'chrysalio.modules.cioskeleton',
            self.configurator.registry['modules'])
        self.assertIsInstance(
            self.configurator.registry['modules'][
                'chrysalio.modules.cioskeleton'],
            ModuleCioSkeleton)

    # -------------------------------------------------------------------------
    def test_dictionary(self):
        """[u:modules.cioskeleton.includeme] with a dictionary"""
        from collections import OrderedDict
        from ....tests import TEST_INI
        from ....security import PRINCIPALS
        from ....scripts import ScriptRegistry
        from .. import includeme, ModuleCioSkeleton

        registry = ScriptRegistry({'__file__': TEST_INI})
        registry['modules'] = OrderedDict()
        registry['principals'] = list(PRINCIPALS)

        includeme(registry)
        self.assertEqual(len(registry['modules']), 1)
        self.assertIn('chrysalio.modules.cioskeleton', registry['modules'])
        self.assertIsInstance(
            registry['modules']['chrysalio.modules.cioskeleton'],
            ModuleCioSkeleton)


# =============================================================================
class UModuleCioSkeleton(TestCase):
    """Unit test class for :class:`modules.cioskeleton.ModuleCioSkeleton`."""

    # -------------------------------------------------------------------------
    def test_activate(self):
        """[u:modules.cioskeleton.ModuleCioSkeleton.activate]"""
        from ....tests import TEST_INI
        from ....security import PRINCIPALS
        from ....menu import MENU_HOME, MENU_ADMIN
        from ....modes import MODE_HOME
        from ..security import PRINCIPALS_CIOSKELETON
        from ..menu import MENU_CIOSKELETON
        from ..modes import MODE_CIOSKELETON
        from .. import ModuleCioSkeleton

        registry = {
            'principals': list(PRINCIPALS), 'menu': [MENU_HOME, MENU_ADMIN]}
        ModuleCioSkeleton(TEST_INI).activate(registry, None)
        self.assertIn(PRINCIPALS_CIOSKELETON[1], registry['principals'])
        self.assertIn(MENU_CIOSKELETON, registry['menu'])

        registry['modes'] = [MODE_HOME]
        ModuleCioSkeleton(TEST_INI).activate(registry, None)
        self.assertIn(MODE_CIOSKELETON, registry['modes'])

    # -------------------------------------------------------------------------
    def test_deactivate(self):
        """[u:modules.cioskeleton.ModuleCioSkeleton.deactivate]"""
        from ....tests import TEST_INI
        from ....security import PRINCIPALS
        from ....modes import MODE_HOME
        from ....menu import MENU_HOME, MENU_ADMIN
        from ..security import PRINCIPALS_CIOSKELETON
        from ..modes import MODE_CIOSKELETON
        from ..menu import MENU_CIOSKELETON
        from .. import ModuleCioSkeleton

        registry = {
            'principals': list(PRINCIPALS), 'menu': [MENU_HOME, MENU_ADMIN]}
        registry['menu'].insert(-1, MENU_CIOSKELETON)
        ModuleCioSkeleton(TEST_INI).deactivate(registry, None)
        self.assertNotIn(PRINCIPALS_CIOSKELETON[1], registry['principals'])
        self.assertNotIn(MENU_CIOSKELETON, registry['menu'])

        registry['modes'] = [MODE_HOME, MODE_CIOSKELETON]
        registry['principals'].append(PRINCIPALS_CIOSKELETON[1])
        ModuleCioSkeleton(TEST_INI).deactivate(registry, None)
        self.assertNotIn(PRINCIPALS_CIOSKELETON[1], registry['principals'])
        self.assertNotIn(MODE_CIOSKELETON, registry['modes'])
