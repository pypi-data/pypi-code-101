"""An exemple of a module which generates conflict with SkeletonModule."""

from ...modules import Module


# =============================================================================
def includeme(configurator):
    """Function to register the module.

    :type  configurator: :pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    # Registration
    Module.register(configurator, ConflictModule)


# =============================================================================
class ConflictModule(Module):
    """Class for Chrysalio module."""

    name = 'Conflict'
    implements = ('skeleton',)
