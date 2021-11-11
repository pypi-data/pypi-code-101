"""CIOLDAP route definitions."""


# =============================================================================
def includeme(configurator):
    """Function to include routes.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    configurator.add_route('cioldap_edit', '/cioldap/edit')
    configurator.add_route('cioldap_view', '/cioldap/view')
