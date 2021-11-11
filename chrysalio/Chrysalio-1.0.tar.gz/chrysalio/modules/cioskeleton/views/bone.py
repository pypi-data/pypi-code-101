"""Bone view callables."""

from pyramid.view import view_config

from ....lib.i18n import _
from ....views import BaseView
from .. import Module


# =============================================================================
class BoneView(BaseView):
    """Class to show how to add views with a module.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """

    # -------------------------------------------------------------------------
    @view_config(
        route_name='bone_index',
        renderer='chrysalio:modules/cioskeleton/Templates/bone_index.pt',
        permission='bone-view')
    def index(self):
        """List all bones."""
        Module.check_activated(self._request, 'chrysalio.modules.cioskeleton')
        self._request.breadcrumbs(_('Bone Management'), 2)
        return {}
