# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioldap`` classes and functions."""

from unittest import TestCase

from ....tests import ModuleTestCase


# =============================================================================
class UCioLDAPIncludeme(ModuleTestCase):
    """Unit test class for :func:`modules.cioldap.includeme`."""

    # -------------------------------------------------------------------------
    def test_configurator(self):
        """[u:modules.cioldap.includeme] with a configurator"""
        from ....tests import TEST_INI
        from .. import includeme, ModuleCioLDAP

        self.configurator.get_settings().update({
            'ldap.base': 'dc=demo1,dc=freeipa,dc=org',
            'ldap.user.dn':
            'uid=_UID_,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org'})

        self.configurator.get_settings()['__file__'] = TEST_INI
        includeme(self.configurator)
        self.assertTrue(self.configurator.registry['modules'])
        self.assertIn(
            'chrysalio.modules.cioldap', self.configurator.registry['modules'])
        self.assertIsInstance(
            self.configurator.registry['modules']['chrysalio.modules.cioldap'],
            ModuleCioLDAP)

    # -------------------------------------------------------------------------
    def test_dictionary(self):
        """[u:modules.cioldap.includeme] with a dictionary"""
        from collections import OrderedDict
        from ....scripts import ScriptRegistry
        from ....tests import TEST_INI
        from .. import includeme, ModuleCioLDAP

        registry = ScriptRegistry({'__file__': TEST_INI})
        registry['modules'] = OrderedDict()

        includeme(registry)
        self.assertEqual(len(registry['modules']), 1)
        self.assertIn('chrysalio.modules.cioldap', registry['modules'])
        self.assertIsInstance(
            registry['modules']['chrysalio.modules.cioldap'], ModuleCioLDAP)


# =============================================================================
class UModuleCioLDAP(TestCase):
    """Unit test class for :class:`modules.cioldap.ModuleCioLDAP`."""

    # -------------------------------------------------------------------------
    def test_activate(self):
        """[u:modules.cioldap.ModuleCioLDAP.activate]"""
        from ....tests import TEST_INI
        from .. import ModuleCioLDAP
        from ..lib.ldap import LDAP
        from ..security import PRINCIPALS_CIOLDAP

        registry = {'principals': []}
        ModuleCioLDAP(TEST_INI).activate(registry, None)
        self.assertIn('principals', registry)
        self.assertIn(PRINCIPALS_CIOLDAP[0], registry['principals'])
        self.assertIn('authorities', registry)
        self.assertIn('ldap', registry['authorities'])
        self.assertIsInstance(registry['authorities']['ldap'], LDAP)

    # -------------------------------------------------------------------------
    def test_deactivate(self):
        """[u:modules.cioldap.ModuleCioLDAP.deactivate]"""
        from ....tests import TEST_INI
        from .. import ModuleCioLDAP
        from ..lib.ldap import LDAP
        from ..security import PRINCIPALS_CIOLDAP

        registry = {
            'principals': [PRINCIPALS_CIOLDAP[0]],
            'authorities': {'ldap': LDAP()}}
        ModuleCioLDAP(TEST_INI).deactivate(registry, None)
        self.assertIn('principals', registry)
        self.assertNotIn(PRINCIPALS_CIOLDAP[0], registry['principals'])
        self.assertIn('authorities', registry)
        self.assertNotIn('ldap', registry['authorities'])
