# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``includes.modules.views`` classes."""

from ....tests import DBUnitTestCase


# =============================================================================
class UIncludesModulesViewsModulesView(DBUnitTestCase):
    """Unit test class for testing
    :class:`includes.modules.views.ModulesView`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ....security import PRINCIPALS
        super(UIncludesModulesViewsModulesView, self).setUp()

        self.configurator.add_route('home', '/home')
        self.configurator.add_route('modules_view', '/modules/view')
        self.configurator.add_route('modules_edit', '/modules/edit')
        self.request.registry['principals'] = list(PRINCIPALS)

    # -------------------------------------------------------------------------
    def test_view(self):
        """[u:includes.modules.views.ModulesView.view]"""
        from collections import namedtuple
        from ..views import ModulesView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='modules_view')

        response = ModulesView(self.request).view()
        self.assertIn('form', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Modules')

    # -------------------------------------------------------------------------
    def test_edit(self):
        """[u:includes.modules.views.ModulesView.edit]"""
        from collections import namedtuple, OrderedDict
        from ..views import ModulesView

        self.request.matched_route = namedtuple('Route', 'name')(
            name='modules_edit')
        self.request.registry['modules'] = OrderedDict()
        self.request.registry['modules_off'] = set()

        response = ModulesView(self.request).edit()
        self.assertIn('form', response)
        self.assertIn('dbmodules', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Modules Edition')

    # -------------------------------------------------------------------------
    def test_edit_save(self):
        """[u:includes.modules.views.ModulesView.edit] save"""
        from collections import OrderedDict
        from ....tests import TEST_INI
        from ....modules.cioskeleton import ModuleCioSkeleton
        from ..models import DBModule
        from ..views import ModulesView

        self.request.registry['modules'] = OrderedDict((
            ('chrysalio.modules.cioskeleton', ModuleCioSkeleton(TEST_INI)),))
        self.request.registry['modules_off'] = set(
            ['chrysalio.modules.cioskeleton'])
        self.request.POST = {
            'chrysalio.modules.cioskeleton': True, 'sav!.x': True}

        ModulesView(self.request).edit()
        dbmodule = self.request.dbsession.query(DBModule).first()
        self.assertIsNone(dbmodule)
        self.assertNotIn(
            'chrysalio.modules.cioskeleton',
            self.request.registry['modules_off'])

    # -------------------------------------------------------------------------
    def test_save(self):
        """[u:includes.modules.views.ModulesView._save]"""
        from collections import OrderedDict
        from ....tests import TEST_INI
        from ....modules import Module
        from ..views import ModulesView

        self.request.POST = {'sav!.x': True}
        self.request.session['menu'] = ()
        self.request.session['modes'] = ['home', 'Home', None]
        self.request.registry['modules'] = OrderedDict()
        self.request.registry['modules_off'] = set()

        self.request.POST['module1'] = True
        ModulesView(self.request).edit()
        self.assertEqual(len(self.request.registry['modules_off']), 0)

        module1 = Module(TEST_INI)
        module1.name = 'Module 1'
        module2 = Module(TEST_INI)
        module2.name = 'Module 2'
        module2.dependencies = ('module1',)
        module3 = Module(TEST_INI)
        module3.name = 'Module 3'
        module3.dependencies = ('module2',)
        self.request.registry['modules'] = OrderedDict((
            ('module1', module1), ('module2', module2), ('module3', module3)))
        self.request.registry['modules_off'] = set(
            ['module1', 'module2', 'module3'])

        self.request.POST['module1'] = True
        ModulesView(self.request).edit()
        self.assertEqual(len(self.request.registry['modules_off']), 2)
        self.assertNotIn('module1', self.request.registry['modules_off'])
        self.assertIn('module2', self.request.registry['modules_off'])
        self.assertIn('module3', self.request.registry['modules_off'])

        self.request.POST['module1'] = False
        self.request.POST['module2'] = True
        ModulesView(self.request).edit()
        self.assertEqual(len(self.request.registry['modules_off']), 1)
        self.assertNotIn('module1', self.request.registry['modules_off'])
        self.assertNotIn('module2', self.request.registry['modules_off'])
        self.assertIn('module3', self.request.registry['modules_off'])

        self.request.POST['module1'] = False
        self.request.POST['module2'] = False
        self.request.POST['module3'] = True
        ModulesView(self.request).edit()
        self.assertEqual(len(self.request.registry['modules_off']), 0)

        self.request.POST['module1'] = False
        self.request.POST['module2'] = True
        self.request.POST['module3'] = True
        ModulesView(self.request).edit()
        self.assertEqual(len(self.request.registry['modules_off']), 3)
