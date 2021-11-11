# pylint: disable = import-outside-toplevel
"""Tests of ``modules`` classes and functions."""

from collections import OrderedDict

from lxml import etree

from pyramid.i18n import TranslationString
from pyramid.httpexceptions import HTTPForbidden

from . import DBUnitTestCase
from ..includes.modules.models import DBModule


# =============================================================================
class UModulesModule(DBUnitTestCase):
    """Unit test class for :class:`modules.Module`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ..security import PRINCIPALS

        super(UModulesModule, self).setUp()
        self.configurator.registry['modules'] = OrderedDict()
        self.configurator.registry['modules_off'] = set()
        self.configurator.registry['principals'] = list(PRINCIPALS)

    # -------------------------------------------------------------------------
    def test_register(self):
        """[u:modules.Module.register]"""
        from . import TEST_INI
        from ..scripts import ScriptRegistry
        from ..security import PRINCIPALS
        from ..modules.cioskeleton import ModuleCioSkeleton

        self.configurator.get_settings()['__file__'] = TEST_INI
        ModuleCioSkeleton.register(self.configurator, ModuleCioSkeleton)
        self.assertEqual(len(self.configurator.registry['modules']), 1)

        registry = ScriptRegistry({'__file__': TEST_INI})
        registry['principals'] = list(PRINCIPALS)
        registry['modules'] = OrderedDict()
        ModuleCioSkeleton.register(registry, ModuleCioSkeleton)
        self.assertEqual(len(registry['modules']), 1)

    # -------------------------------------------------------------------------
    def test_check_conflicts(self):
        """[u:modules.Module.check_conflicts]"""
        from . import TEST_INI
        from ..modules import Module

        module1 = Module(TEST_INI)
        module1.implements = ('foo', 'bar')
        module2 = Module(TEST_INI)
        includes = ('chrysalio.includes.themes', 'module1', 'module2')
        modules = OrderedDict((('module1', module1), ('module2', module2)))

        implementations, error = Module.check_conflicts(includes, modules)
        self.assertIsNone(error)
        self.assertIn('foo', implementations)
        self.assertIn('bar', implementations)
        self.assertIn('module1', implementations)
        self.assertIn('module2', implementations)

        module2.implements = ('bar',)
        implementations, error = Module.check_conflicts(includes, modules)
        self.assertIsInstance(error, TranslationString)
        self.assertEqual(error.mapping['m1'], 'module1')
        self.assertEqual(error.mapping['m2'], 'module2')
        self.assertEqual(error.mapping['f'], 'bar')
        self.assertFalse(implementations)

    # -------------------------------------------------------------------------
    def test_check_dependencies(self):
        """[u:modules.Module.check_dependencies]"""
        from . import TEST_INI
        from ..modules import Module

        module = Module(TEST_INI)

        self.assertIsNone(module.check_dependencies(
            ('chrysalio.includes.themes',)))

        module.dependencies = ('chrysalio.includes.themes',)
        self.assertIsNone(module.check_dependencies(
            ('chrysalio.includes.themes', 'chrysalio.modules.foo')))
        self.assertIsNone(module.check_dependencies(
            ('chrysalio.includes.themes',)))
        self.assertIsNotNone(module.check_dependencies(
            ('chrysalio.modules.foo',)))

        module.dependencies = (
            'chrysalio.includes.themes', 'bar-implementation')
        self.assertIsNone(module.check_dependencies(
            ('chrysalio.includes.themes', 'bar-implementation')))
        self.assertIsNotNone(module.check_dependencies(
            ('chrysalio.includes.themes',)))

    # -------------------------------------------------------------------------
    def test_check_activations(self):
        """[u:modules.Module.check_activations]"""
        from . import TEST_INI
        from ..modules import Module

        modules_off = set(['chrysalio.modules'])
        module = Module(TEST_INI)
        self.assertFalse(module.check_activations(modules_off))

        modules_off = set(['chrysalio.modules.cioskeleton'])
        module.dependencies = ('chrysalio.modules.cioskeleton',)
        self.assertTrue(module.check_activations(modules_off))

    # -------------------------------------------------------------------------
    def test_module_xml2db(self):
        """[u:modules.Module.module_xml2db]"""
        from . import TEST_INI
        from ..modules import Module

        def _xml2db(dbsession, root_elt, only, error_if_exists):
            """Dummy xml2db function."""
            # pylint: disable = unused-argument
            return []

        dbsession = self.request.dbsession
        tree = etree.XML(
            '<chrysalio version="1.0">'
            '  <module id="chrysalio.modules.cioskeleton" inactive="true"/>'
            '</chrysalio>')
        module = Module(TEST_INI)
        module.uid = 'chrysalio.modules.cioskeleton'

        # Without _DBModule and settings
        self.assertFalse(module.module_xml2db(dbsession, tree, None, False))
        self.assertIsNone(dbsession.query(DBModule).filter_by(
            module_id=module.uid).first())

        # Inactive module
        # pylint: disable = protected-access
        module._DBModule = DBModule
        # pylint: enable = protected-access
        errors = module.module_xml2db(dbsession, tree, None, False)
        self.assertFalse(errors)
        self.assertIsNotNone(dbsession.query(DBModule).filter_by(
            module_id=module.uid).first())

        # Active module
        tree = etree.XML(
            '<chrysalio version="1.0">'
            '  <module id="chrysalio.modules.cioskeleton" inactive="false"/>'
            '</chrysalio>')
        self.assertFalse(module.module_xml2db(dbsession, tree, None, False))
        self.assertIsNone(dbsession.query(DBModule).filter_by(
            module_id=module.uid).first())

        # Without settings
        tree = etree.XML(
            '<chrysalio version="1.0">'
            '  <module id="foo" inactive="true"/>'
            '</chrysalio>')
        module.relaxng = {
            'namespace': 'http://ns.chrysal.io/chrysalio/skeleton',
            'root': 'chrysalio-skeleton'}
        module.xml2db = (_xml2db,)
        self.assertFalse(module.module_xml2db(dbsession, tree, None, False))

        # With settings in a backup
        tree = etree.XML(
            '<chrysalio version="1.0">'
            '  <module id="chrysalio.modules.cioskeleton" inactive="true">'
            '    <chrysalio-skeleton'
            '        xmlns="http://ns.chrysal.io/chrysalio/skeleton"'
            '        version="1.0">'
            '      <bones>'
            '        <bone id="hand"><label>Hand</label></bone>'
            '      </bones>'
            '    </chrysalio-skeleton>'
            '  </module>'
            '</chrysalio>')
        self.assertFalse(module.module_xml2db(dbsession, tree, None, False))

        # With settings in a simple configuration
        tree = etree.XML(
            '<chrysalio-skeleton'
            '    xmlns="http://ns.chrysal.io/chrysalio/skeleton"'
            '    version="1.0">'
            '  <bones>'
            '    <bone id="hand"><label>Hand</label></bone>'
            '  </bones>'
            '</chrysalio-skeleton>')
        self.assertFalse(module.module_xml2db(dbsession, tree, None, False))

    # -------------------------------------------------------------------------
    def test_module_db2xml(self):
        """[u:modules.Module.module_db2xml]"""
        from . import TEST_INI
        from ..modules import Module

        def _db2xml(dbsession, root_elt):
            """Dummy db2xml function."""
            # pylint: disable = unused-argument, unnecessary-pass
            pass

        dbsession = self.request.dbsession
        module = Module(TEST_INI)
        module.uid = 'chrysalio.modules.cioskeleton'

        # Without _DBModule
        elements = module.module_db2xml(dbsession)
        self.assertEqual(len(elements), 0)

        # Inactive, without settings
        dbsession.add(DBModule(module_id=module.uid, inactive=True))
        # pylint: disable = protected-access
        module._DBModule = DBModule
        # pylint: enable = protected-access
        elements = module.module_db2xml(dbsession)
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0].tag, 'module')
        self.assertEqual(elements[0].get('inactive'), 'true')

        # Without settings
        module.relaxng = {
            'namespace': 'http://ns.chrysal.io/chrysalio/skeleton',
            'root': 'chrysalio-skeleton', 'version': '1.0'}
        module.db2xml = (_db2xml,)
        elements = module.module_db2xml(dbsession)
        self.assertEqual(len(elements), 1)
        self.assertEqual(len(elements[0]), 1)
        self.assertEqual(
            elements[0][0].tag,
            '{http://ns.chrysal.io/chrysalio/skeleton}chrysalio-skeleton')

    # -------------------------------------------------------------------------
    def test_poppulate(self):
        """[u:modules.Module.populate]"""
        from . import TEST_INI
        from ..modules import Module

        dbsession = self.request.dbsession
        self.assertIsNone(Module(TEST_INI).populate({}, {}, dbsession))

    # -------------------------------------------------------------------------
    def test_backup(self):
        """[u:modules.Module.backup]"""
        from . import TEST_INI, BACKUP_DIR
        from ..modules import Module

        dbsession = self.request.dbsession
        self.assertIsNone(
            Module(TEST_INI).backup({}, {}, dbsession, BACKUP_DIR))

    # -------------------------------------------------------------------------
    def test_activate(self):
        """[u:modules.Module.activate]"""
        from . import TEST_INI
        from ..modules import Module

        dbsession = self.request.dbsession
        self.assertIsNone(Module(TEST_INI).activate({}, dbsession))

    # -------------------------------------------------------------------------
    def test_deactivate(self):
        """[u:modules.Module.deactivate]"""
        from . import TEST_INI
        from ..modules import Module

        dbsession = self.request.dbsession
        self.assertIsNone(Module(TEST_INI).deactivate({}, dbsession))

    # -------------------------------------------------------------------------
    def test_check_activated(self):
        """[u:modules.Module.check_activated]"""
        from ..modules import Module

        self.assertRaises(
            HTTPForbidden, Module.check_activated, self.request,
            'chrysalio.modules.cioskeleton')

    # -------------------------------------------------------------------------
    def test_configuration_route(self):
        """[u:modules.Module.configuration_route]"""
        from . import TEST_INI
        from ..modules import Module

        self.assertIsNone(Module(TEST_INI).configuration_route(self.request))

    # -------------------------------------------------------------------------
    def test_settings(self):
        """[u:modules.Module._settings]"""
        from . import TEST_INI
        from ..modules import Module

        # With standard section
        # pylint: disable = protected-access
        settings = Module(TEST_INI)._settings(TEST_INI)
        # pylint: enable = protected-access
        self.assertIsInstance(settings, dict)
        self.assertIn('here', settings)

        # With CioFoo section
        # pylint: disable = protected-access
        settings = Module(TEST_INI)._settings(TEST_INI, 'CioFoo')
        # pylint: enable = protected-access
        self.assertIn('here', settings)
        self.assertIn('bar', settings)
