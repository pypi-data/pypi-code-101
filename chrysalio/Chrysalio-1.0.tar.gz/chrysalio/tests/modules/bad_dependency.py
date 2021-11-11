"""An exemple of a module with unsatisfied dependency."""

from ...modules import Module


# =============================================================================
def includeme(configurator):
    """Function to register the module.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    # Registration
    Module.register(configurator, BadDependencyModule)


# =============================================================================
class BadDependencyModule(Module):
    """Class for Chrysalio module."""

    name = 'Bad dependencies'
    dependencies = ('chrysalio.modules.foo',)
