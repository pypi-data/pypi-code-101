"""CioSkeleton route definitions."""


# =============================================================================
def includeme(configurator):
    """Function to include routes.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    configurator.add_route('bone_index', '/bone/index')
