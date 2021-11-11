# pylint: disable = import-outside-toplevel
"""Tests of ``includes.modules.models.DBModule`` class."""

from ....tests import DBUnitTestCase


# =============================================================================
class UIncludesModulesModelsDBModule(DBUnitTestCase):
    """Unit test class for :class:`includes.modules.models.DBModule`."""

    # -------------------------------------------------------------------------
    def test_table4view(self):
        """[u:includes.modules.models.DBModule.table4view]"""
        from collections import OrderedDict
        from ....tests import TEST_INI
        from ....modules.cioldap import ModuleCioLDAP
        from ..models import DBModule

        html = DBModule.table4view(self.request)
        self.assertEqual(html, 'No module.')

        self.configurator.add_route('cioldap_view', '/cioldap/view')
        self.request.registry['modules'] = OrderedDict((
            ('chrysalio.modules.cioldap', ModuleCioLDAP(TEST_INI)),))
        self.request.registry['modules_off'] = set()

        html = DBModule.table4view(self.request)
        self.assertIn('title="chrysalio.modules.cioldap"', html)
        self.assertIn('>LDAP</', html)

    # -------------------------------------------------------------------------
    def test_settings_schema(self):
        """[u:includes.modules.models.DBModule.settings_schema]"""
        from collections import OrderedDict
        from colander import SchemaNode
        from ....tests import TEST_INI
        from ....modules.cioskeleton import ModuleCioSkeleton
        from ..models import DBModule

        self.request.registry['modules'] = OrderedDict((
            ('chrysalio.modules.cioskeleton', ModuleCioSkeleton(TEST_INI)),))
        self.request.registry['modules_off'] = set()

        schema, defaults = DBModule.settings_schema(self.request)
        self.assertIsInstance(schema, SchemaNode)
        self.assertIn('chrysalio.modules.cioskeleton', schema.serialize())
        self.assertIsInstance(defaults, dict)
        self.assertIn('chrysalio.modules.cioskeleton', defaults)
        self.assertTrue(defaults['chrysalio.modules.cioskeleton'])

    # -------------------------------------------------------------------------
    def test_table4edit(self):
        """[u:includes.modules.models.DBModule.table4edit]"""
        from collections import OrderedDict
        from ....tests import TEST_INI
        from ....lib.form import Form
        from ....modules.cioskeleton import ModuleCioSkeleton
        from ..models import DBModule

        html = DBModule.table4edit(self.request, Form(self.request))
        self.assertEqual(html, 'No module.')

        self.request.registry['modules'] = OrderedDict((
            ('chrysalio.modules.cioskeleton', ModuleCioSkeleton(TEST_INI)),))
        self.request.registry['modules_off'] = set(
            ['chrysalio.modules.cioskeleton'])

        html = DBModule.table4edit(self.request, Form(self.request))
        self.assertIn('chrysalio.modules.cioskeleton', html)
        self.assertIn('>Skeleton</', html)
