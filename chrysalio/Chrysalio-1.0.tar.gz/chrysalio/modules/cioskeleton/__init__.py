"""An example of a module for Chrysalio with dependencies, permissions, routes,
views and menu."""

from os.path import dirname, join

from pyramid.config import Configurator

from ...lib.i18n import _
from ...includes.modules.models import DBModule
from .. import Module
from .relaxng import RELAXNG_CIOSKELETON
from .security import PRINCIPALS_CIOSKELETON
from .menu import MENU_CIOSKELETON
from .modes import MODE_CIOSKELETON
from .models.populate import xml2db as _xml2db, db2xml as _db2xml


# =============================================================================
def includeme(configurator):
    """Function to register the module.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    # Registration
    Module.register(configurator, ModuleCioSkeleton)
    if not isinstance(configurator, Configurator):
        return

    # Permissions
    configurator.include('chrysalio.modules.cioskeleton.security')

    # Routes
    configurator.include('chrysalio.modules.cioskeleton.routes')

    # Views
    for theme in configurator.registry['themes']:
        theme = '/theme/{0}'.format(theme.lower()) if theme else ''
        path = '{0}/cioskeleton/images/'.format(theme)
        if configurator.introspector.get('static views', path) is None:
            configurator.add_static_view(
                path, join(dirname(__file__), 'Static', 'Images'))
        path = '{0}/cioskeleton/css/'.format(theme)
        if configurator.introspector.get('static views', path) is None:
            configurator.add_static_view(
                path, join(dirname(__file__), 'Static', 'Css'))
    configurator.scan('chrysalio.modules.cioskeleton.views')


# =============================================================================
class ModuleCioSkeleton(Module):
    """Class for an example of Chrysalio module.

    :param str config_ini:
        Absolute path to the configuration file (e.g. development.ini).
    """

    name = _('Skeleton')
    implements = ('skeleton',)
    dependencies = ('chrysalio.includes.themes',)
    relaxng = RELAXNG_CIOSKELETON
    xml2db = (_xml2db,)
    db2xml = (_db2xml,)
    _DBModule = DBModule

    # -------------------------------------------------------------------------
    def activate(self, registry, dbsession):
        """Method to activate the module.

        :type  registry: pyramid.registry.Registry
        :param registry:
            Application registry.
        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        """
        if registry['principals'][0][0] == 'mode' and \
           PRINCIPALS_CIOSKELETON[0][2][0] not in registry['principals'][0][2]:
            registry['principals'][0][2].append(
                PRINCIPALS_CIOSKELETON[0][2][0])
        if PRINCIPALS_CIOSKELETON[1] not in registry['principals']:
            registry['principals'].append(PRINCIPALS_CIOSKELETON[1])

        if 'modes' in registry and MODE_CIOSKELETON not in registry['modes']:
            registry['modes'].insert(1, MODE_CIOSKELETON)
        elif 'menu' in registry and MENU_CIOSKELETON not in registry['menu']:
            registry['menu'].insert(1, MENU_CIOSKELETON)

    # -------------------------------------------------------------------------
    def deactivate(self, registry, dbsession):
        """Method to deactivate the module.

        :type  registry: pyramid.registry.Registry
        :param registry:
            Application registry.
        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        """
        if registry['principals'][0][0] == 'mode' and \
           PRINCIPALS_CIOSKELETON[0][2][0] in registry['principals'][0][2]:
            registry['principals'][0][2].remove(
                PRINCIPALS_CIOSKELETON[0][2][0])
        if PRINCIPALS_CIOSKELETON[1] in registry['principals']:
            registry['principals'].remove(PRINCIPALS_CIOSKELETON[1])

        if 'modes' in registry and MODE_CIOSKELETON in registry['modes']:
            registry['modes'].remove(MODE_CIOSKELETON)
        elif 'menu' in registry and MENU_CIOSKELETON in registry['menu']:
            registry['menu'].remove(MENU_CIOSKELETON)
