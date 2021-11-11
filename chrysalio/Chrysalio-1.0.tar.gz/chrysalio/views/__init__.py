"""Base class for view callables."""

from ..lib.panel import Panel


# =============================================================================
class BaseView(object):
    """Base class to manage with panel.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    # pylint: disable = too-few-public-methods

    # -------------------------------------------------------------------------
    def __init__(self, request):
        """Constructor method."""
        self._request = request
        Panel.manage_panels(request)
