"""Modules management."""

from collections import OrderedDict

from transaction import manager

from pyramid.config import Configurator

from ...lib.i18n import _
from ...lib.config import update_acl
from ...menu import MENU_ADMIN
from ...models import DB_METADATA, get_tm_dbsession
from .models import DBModule


PRINCIPALS_MODULES = (
    ('modules', _('Module management'), (
        ('viewer', _('View any module'), ('modules-view',)),
        ('editor', _('Edit or view any module'), (
            'modules-edit', 'modules-view'))
    )),
)
SUBMENU_MODULES = (
    None, _('Modules'), 'modules-view', 'modules_view', None)


# =============================================================================
def includeme(configurator):
    """Function to include modules functionality.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    # Populate/backup
    if not isinstance(configurator, Configurator):
        return

    # Routes
    configurator.add_route('modules_view', '/modules/view')
    configurator.add_route('modules_edit', '/modules/edit')

    # Premissions
    update_acl(configurator, PRINCIPALS_MODULES)
    if PRINCIPALS_MODULES[0] not in configurator.registry['principals']:
        configurator.registry['principals'].append(PRINCIPALS_MODULES[0])

    # Menu
    if 'modes' in configurator.registry:
        mode = dict(configurator.registry['modes']).get('admin')
        if mode is not None:
            mode[4][4].insert(0, SUBMENU_MODULES)
    elif 'menu' in configurator.registry and \
         MENU_ADMIN in configurator.registry['menu']:
        admin_menu = configurator.registry['menu'][
            configurator.registry['menu'].index(MENU_ADMIN)]
        admin_menu[4].insert(0, SUBMENU_MODULES)

    # Views
    configurator.scan('chrysalio.includes.modules.views')

    # Database table and Registry
    configurator.registry['modules'] = OrderedDict()
    configurator.registry['modules_off'] = set()
    with manager:
        dbsession = get_tm_dbsession(
            configurator.registry['dbsession_factory'], manager)
        DB_METADATA.create_all()
        for dbmodule in dbsession.query(DBModule):
            if dbmodule.inactive:
                configurator.registry['modules_off'].add(dbmodule.module_id)
