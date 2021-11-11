"""CioLDAP, a module to manage LDAP authentication."""

from pyramid.config import Configurator

from ...lib.i18n import _
from ...includes.modules.models import DBModule
from .. import Module
from .relaxng import RELAXNG_CIOLDAP
from .security import PRINCIPALS_CIOLDAP
from .lib.ldap import LDAP
from .models.populate import xml2db as _xml2db, db2xml as _db2xml


# =============================================================================
def includeme(configurator):
    """Function to register the module.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    # Registration
    Module.register(configurator, ModuleCioLDAP)
    if not isinstance(configurator, Configurator):
        return

    # Permission
    configurator.include('chrysalio.modules.cioldap.security')

    # Routes
    configurator.include('chrysalio.modules.cioldap.routes')

    # Views
    configurator.scan('chrysalio.modules.cioldap.views')


# =============================================================================
class ModuleCioLDAP(Module):
    """Class for CioLDAP module.

    :param str config_ini:
        Absolute path to the configuration file (e.g. development.ini).
    """

    name = _('LDAP')
    implements = ('ldap',)
    relaxng = RELAXNG_CIOLDAP
    xml2db = (_xml2db,)
    db2xml = (_db2xml,)
    areas = {}
    _DBModule = DBModule

    # -------------------------------------------------------------------------
    def activate(self, registry, dbsession):
        """Method to activate the module.

        :type  registry: pyramid.regisry.Registry
        :param registry:
            Application registry.
        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        """
        # Security
        if PRINCIPALS_CIOLDAP[0] not in registry['principals']:
            registry['principals'].append(PRINCIPALS_CIOLDAP[0])

        # Authorities
        if 'authorities' not in registry:
            registry['authorities'] = {}
        if 'ldap' not in registry['authorities']:
            registry['authorities']['ldap'] = LDAP()

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
        # Security
        if PRINCIPALS_CIOLDAP[0] in registry['principals']:
            registry['principals'].remove(PRINCIPALS_CIOLDAP[0])

        # Authorities
        if 'authorities' in registry and 'ldap' in registry['authorities']:
            del registry['authorities']['ldap']

    # -------------------------------------------------------------------------
    def configuration_route(self, request):
        """Return the route to configure this module.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        return request.route_path('cioldap_view')
