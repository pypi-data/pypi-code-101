"""View callables."""

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ...lib.i18n import _
from ...lib.log import log_info
from ...lib.form import get_action, Form
from ...lib.menu import Menu
from ...lib.modes import Modes
from ...views import BaseView
from .models import DBModule


# =============================================================================
class ModulesView(BaseView):
    """Class to manage modules.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """

    # -------------------------------------------------------------------------
    @view_config(
        route_name='modules_view',
        renderer='chrysalio:includes/modules/Templates/modules_view.pt',
        permission='modules-view')
    def view(self):
        """Show modules."""
        i_editor = self._request.has_permission('modules-edit')

        self._request.breadcrumbs(
            _('Modules'), 2,
            replace=self._request.route_path('modules_edit'))

        return {
            'form': Form(self._request), 'dbmodules': DBModule,
            'i_editor': i_editor}

    # -------------------------------------------------------------------------
    @view_config(
        route_name='modules_edit',
        renderer='chrysalio:includes/modules/Templates/modules_edit.pt',
        permission='modules-edit')
    def edit(self):
        """Edit modules."""
        form = Form(self._request, *DBModule.settings_schema(self._request))
        action = get_action(self._request)[0]
        if action == 'sav!' and form.validate():
            self._save([k for k in form.values if form.values[k]])
            log_info(self._request, 'modules_edit')
            return HTTPFound(self._request.route_path('modules_view'))

        self._request.breadcrumbs(
            _('Modules Edition'), 2,
            replace=self._request.route_path('modules_view'))

        return {'form': form, 'dbmodules': DBModule, 'action': action}

    # -------------------------------------------------------------------------
    def _save(self, after):
        """Save modules.

        :param list after:
            List of desired active modules after update.
        """
        modules = self._request.registry['modules']
        before = [k for k in modules
                  if k not in self._request.registry['modules_off']]
        active = set()
        to_activate = set()

        # Process newly activated
        for module_id in modules:
            if module_id in after:
                if module_id in before:
                    active.add(module_id)
                else:
                    to_activate.add(module_id)
                    self._activate_module_dependencies(module_id, to_activate)

        # Process newly deactivated
        for module_id in modules:
            if module_id not in after and module_id in before and \
               module_id not in to_activate:
                self._deactivate_module_depending(module_id, active)

        # Modules to activave
        to_activate |= active

        # Activate/deactivate modules and update modules table
        self._update_modules(modules, to_activate)

        # Update modes and menu
        Modes.invalidate(self._request, 'modes')
        Menu.invalidate(self._request, 'menu')

    # -------------------------------------------------------------------------
    def _update_modules(self, modules, to_activate):
        """Activate/deactivate modules and update modules table.

        :type  modules: OrderedDict
        :param modules:
            Dictionary of available modules.
        :param set to_activate:
            Set of modules to activate.
        """
        before = [k for k in self._request.registry['modules']
                  if k not in self._request.registry['modules_off']]
        for module_id in modules:
            newly_active = module_id in to_activate

            if newly_active and module_id not in before:
                modules[module_id].activate(
                    self._request.registry, self._request.dbsession)
                self._request.registry['modules_off'].remove(module_id)
            elif not newly_active and module_id in before:
                modules[module_id].deactivate(
                    self._request.registry, self._request.dbsession)
                self._request.registry['modules_off'].add(module_id)

            dbmodule = self._request.dbsession.query(DBModule).filter_by(
                module_id=module_id).first()
            if newly_active and dbmodule is not None:
                self._request.dbsession.delete(dbmodule)
            elif not newly_active and dbmodule is None:
                self._request.dbsession.add(DBModule(
                    module_id=module_id, inactive=True))

    # -------------------------------------------------------------------------
    def _activate_module_dependencies(self, module_id, activated):
        """Recursive method to activate dependencies of the module
        ``module_id``.

        :param str module_id:
            ID of the reference module.
        :param set activated:
            Set of already activated moodules
        """
        modules = self._request.registry['modules']
        for depend_id in modules[module_id].dependencies:
            if depend_id in modules and depend_id not in activated:
                activated.add(depend_id)
                self._activate_module_dependencies(depend_id, activated)

    # -------------------------------------------------------------------------
    def _deactivate_module_depending(self, module_id, active):
        """Recursive method to deactivate modules depending on the module
        ``module_id``.

        :param str module_id:
            ID of the reference module.
        :param set activated:
            Set of already activated moodules
        """
        for active_id in active.copy():
            if module_id in self._request.registry[
                    'modules'][active_id].dependencies:
                active.remove(active_id)
                self._deactivate_module_depending(active_id, active)
