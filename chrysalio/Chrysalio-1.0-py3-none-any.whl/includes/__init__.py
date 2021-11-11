"""Collection of functionalities with an `includeme()` function to be used by
the Pyramid configurator or in the INI file."""

from sys import exit as sys_exit

from transaction import manager

from ..lib.i18n import _, translate
from ..lib.config import settings_get_list
from ..modules import Module
from ..models import get_tm_dbsession


# =============================================================================
def load_includes(configurator, includes=None):
    """Load modules with an `includeme()` function and fill
    ``configurator.registry['modules']`` ordered dictionary.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    :param list includes: (optional)
        List of hard coding `includes`.
    """
    # Load includes and modules
    settings = configurator.get_settings()
    if includes is None:
        includes = []
    includes += [
        k for k in settings_get_list(settings, 'chrysalio.includes') if k]
    for include in includes:
        try:
            configurator.include(include)
        except ImportError as error:
            sys_exit(translate(
                _('*** Unable to load module "${m}" [${e}]', {
                    'm': include, 'e': error})))

    # Check modules
    if configurator.registry.get('modules'):
        # Check conflicts
        modules = configurator.registry['modules']
        implementations, error = Module.check_conflicts(includes, modules)
        if error is not None:
            sys_exit(translate(error))

        # Check dependencies
        for module_id in modules:
            error = modules[module_id].check_dependencies(implementations)
            if error is not None:
                sys_exit(translate(error))

        # Check activations
        activation = True
        while activation:
            activation = False
            for module_id in modules:
                activation |= modules[module_id].check_activations(
                    configurator.registry['modules_off'])

        # Activate modules
        with manager:
            dbsession = get_tm_dbsession(
                configurator.registry['dbsession_factory'], manager)
            for module_id in modules:
                if module_id not in configurator.registry['modules_off']:
                    modules[module_id].activate(
                        configurator.registry, dbsession)
