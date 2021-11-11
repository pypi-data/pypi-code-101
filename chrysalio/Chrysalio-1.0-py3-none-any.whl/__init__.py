"""The :func:`.main` function is called when the ``pserve`` command is invoked
against this application.
"""
from pyramid.config import Configurator

from .initialize import Initialize
from .lib.i18n import locale_negotiator
from .includes import load_includes


# =============================================================================
def main(global_config, **settings):
    """This function returns a Pyramid WSGI application.

    :param dict global_config:
        Dictionary describing the INI file with keys ``__file__`` and ``here``.
    :param dict settings:
        Application settings of [app:main] section of INI file.
    :rtype: pyramid.router.Router
    :return:
        WSGI application.
    """
    configurator = Configurator(
        settings=settings,
        locale_negotiator=locale_negotiator,
        default_permission='authenticated')

    # Chrysalio configuration
    configurator.include('pyramid_chameleon')
    configurator.include('.relaxng')
    configurator.include('.models')
    configurator.include('.routes')
    configurator.include('.security')
    configurator.include('.subscribers')
    configurator.scan('.views')
    Initialize(configurator).complete(
        global_config, __package__, 'ciopopulate')
    configurator.commit()

    # Includes loading
    load_includes(configurator)

    return configurator.make_wsgi_app()
