"""Class to manage modes."""

from webhelpers2.html import literal
from pyramid.httpexceptions import HTTPNotFound, HTTPForbidden

from ..includes.themes import theme_static_prefix
from ..lib.i18n import _


# =============================================================================
class Modes(object):
    """Modes base class.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str uid:
        Unique ID used to store the mode in the session.
    :param list framework:
        Full version of the mode.

    The framework of the mode is a list of available modes. Each item of the
    list has the following structure:

        mode = (mode_id, (icon, label, permission, route, menu))

    ``route`` can be a name of route, a tuple such as
    ``(route_name, params_dict)`` or a function returning such a tuple.

    ``menu`` can be a list of menu entries or a function returning such a
    list.

    In the user session, under ``uid`` key, modes are stored as a list
    ``[current_mode_id, current_label, modes]``. ``modes`` is a list of modes
    filtered according to user permissions.
    """

    # -------------------------------------------------------------------------
    def __init__(self, request, uid, framework):
        """Constructor method."""
        self._request = request
        self.uid = uid
        self._framework = framework

    # -------------------------------------------------------------------------
    def label(self):
        """Return the translated label of the current mode.

        :rtype: str
        """
        self._construct()
        return self._request.session[self.uid][1]

    # -------------------------------------------------------------------------
    def menu_framework(self):
        """Return the framework of the menu.

        :rtype: tuple
        """
        if self.uid not in self._request.session:
            mode = self._framework[0]
            return mode[1][4][4] or () if mode[1][4] else ()

        current_mode_id = self._request.session[self.uid][0]
        for mode in self._framework:
            if mode[0] == current_mode_id:
                return mode[1][4][4] or () if mode[1][4] else ()
        return ()

    # -------------------------------------------------------------------------
    def select(self, mode_id):
        """Select a new mode.

        :param str mode_id:
            ID of menu to select.
        :rtype: str
        :return:
            Return the default route for the selected mode.
        """
        mode = dict(self._framework).get(mode_id)
        if mode is None:
            raise HTTPNotFound(comment=_('Unknown mode ${m}.', {'m': mode_id}))

        if mode[2] is not None and not self._request.has_permission(mode[2]):
            raise HTTPForbidden()

        self._request.session[self.uid] = [
            mode_id, self._request.localizer.translate(mode[1]), None]
        self._construct()

        route = mode[3] if isinstance(mode[3], (list, tuple)) \
            else (mode[3], {})
        return self._request.route_path(route[0], **route[1])

    # -------------------------------------------------------------------------
    def xhtml(self):
        """Return a <ul> structure with the list of modes.

        :rtype: webhelpers2.html._literal.literal
        """
        self._construct()
        return self._request.session[self.uid][2]

    # -------------------------------------------------------------------------
    @classmethod
    def invalidate(cls, request, uid):
        """Invalidate the mode ``uid`` if exists.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str uid:
            Unique ID of the mode to invalidate.
        """
        if uid in request.session:
            request.session[uid][2] = None

    # -------------------------------------------------------------------------
    def _construct(self):
        """If the mode does not exist in session, construct it according to
        user permissions and put it in ``session[self.uid]``."""
        # Mode in session
        if self.uid in self._request.session and \
           self._request.session[self.uid][2] is not None:
            return

        # List of modes
        theme = theme_static_prefix(self._request)
        translate = self._request.localizer.translate
        current_mode_id = None
        current_label = None
        authorized = set()
        html = ''
        for mode in self._framework:
            if not self._has_permission(mode):
                continue
            label = translate(mode[1][1])
            if current_mode_id is None:
                current_mode_id = mode[0]
                current_label = label
            html += '<li><span><a href="{url}">'.format(
                url=self._request.route_path('mode', mode_id=mode[0]))
            if mode[1][0]:  # icon
                html += '<img src="{icon}" alt="{label}"'\
                    ' title="{label}"/> '.format(
                        icon=mode[1][0].format(theme=theme), label=label)
            html += '{label}</a></span></li>'.format(label=label)
            authorized.add(mode[0])
        if not html:
            self._request.session[self.uid] = [None, '', html]
            return
        html = '<ul id="cioModes-{uid}">{html}</ul>'.format(
            uid=self.uid, html=html) if len(authorized) > 1 else ''

        # Default mode
        if self.uid in self._request.session and \
           self._request.session[self.uid][0] in authorized:
            current_mode_id = self._request.session['modes'][0]
            current_label = self._request.session['modes'][1]

        # Session
        self._request.session[self.uid] = [
            current_mode_id, current_label, literal(html)]

    # -------------------------------------------------------------------------
    def _has_permission(self, mode):
        """Check if the user has the permission to use this mode.

        :param tuple mode:
            The mode to check.
        :rtype: bool
        """
        if mode[1][2] is None:
            return True
        return self._request.has_permission(mode[1][2]).boolval
