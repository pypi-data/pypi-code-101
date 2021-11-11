"""Class to manage user menus."""

from webhelpers2.html import literal

from ..includes.themes import theme_static_prefix
from .utils import make_id
from .breadcrumbs import DEFAULT_ROOT_CHUNKS


# =============================================================================
class Menu(object):
    """User menu base class.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str uid:
        Unique ID used to store the menu in the session.
    :param list framework:
        Full version of the menu.

    The framework of the menu is a list of pieces. Each piece has the
    following structure:

        piece = (icon, label, permission, route, (subentry, ...))

    ``route`` can be a name of route or a tuple such as
    ``(route_name, params_dict)``.

    In the user session, under ``uid`` key, pieces are filtered according to
    user permissions and converted into menu entries. In an entry:

    * ``label`` is translated
    * ``permission`` is replaced by the final route.
    """

    # -------------------------------------------------------------------------
    def __init__(self, request, uid, framework):
        """Constructor method."""
        self._request = request
        self.uid = uid
        self._framework = framework

    # -------------------------------------------------------------------------
    def is_empty(self):
        """Return ``True`` if current menu is empty.

         :rtype: bool
        """
        self._construct()
        return not bool(self._request.session[self.uid])

    # -------------------------------------------------------------------------
    def xhtml(self, **kwargs):
        """Return an <ul> structure with current entry highlighted.

        :rtype:  webhelpers2.html._literal.literal

        Options are:

        - no_icon=True: suppress icons in entries
        - tooltip=True: add attribute 'title' on entries span
        """
        self._construct()

        crumb_trail = \
            (hasattr(self._request, 'breadcrumbs') and
             self._request.breadcrumbs.crumb_trail()) or \
            (self._request.matched_route is not None and
             [(self._request.current_route_path().partition('?')[0].split('/')[
                 1:DEFAULT_ROOT_CHUNKS + 1], DEFAULT_ROOT_CHUNKS)]) or []

        html = self._xhtml_entries(
            theme_static_prefix(self._request), 0,
            self._request.session[self.uid], crumb_trail, kwargs)

        return literal(
            '<ul id="cioMenu-{uid}" role="menu">{menu}</ul>'.format(
                uid=self.uid, menu=html)) if html else ''

    # -------------------------------------------------------------------------
    @classmethod
    def invalidate(cls, request, uid):
        """Invalidate the menu ``uid`` if exists.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str uid:
            Unique ID of the menu to invalidate.
        """
        if uid in request.session:
            del request.session[uid]

    # -------------------------------------------------------------------------
    def _construct(self):
        """If the menu does not exist in session, construct it according to
        user permissions and put it in ``session[self.uid]``."""
        # Menu in session
        if self.uid in self._request.session:
            return

        # Construction
        menu = []
        for piece in self._framework:
            if self._has_permission(piece):
                entry = self._entry(piece)
                if entry is not None:
                    menu.append(entry)

        self._request.session[self.uid] = tuple(menu)

    # -------------------------------------------------------------------------
    def _xhtml_entries(self, theme, depth, entries, crumb_trail, options):
        """Return <li> tags with entries.

        :param str theme:
             URL prefix for the current theme.
        :param int depth:
            Depth of entries in menu.
        :param tuple entries:
            Tuple of entry tuples (See :meth:`_entry`)
        :param list crumb_trail:
            List of crumbs in the breadcrumb trail
            (See :meth:`~chrysalio.lib.breadcrumbs.Breadcrumbs.crumb_trail`).
        :param dict options:
            Dictionary of options to configure the menu.
        """
        html = ''
        for entry in entries:
            html += '<li class="cioDepth{depth}">'\
                '<span class="cioMenu-{class_}{current}"{title}>'.format(
                    class_=entry[0],
                    depth=depth,
                    current=' cioCurrent' if self._is_current(
                        crumb_trail, entry) else '',
                    title=' title="{0}"'.format(entry[2])
                    if options or options.get('tooltip') else '')
            # URL
            if entry[3]:
                html += '<a href="{url}"{blank}>'.format(
                    url=entry[3],
                    blank=entry[4] == 'blank' and ' target="_blank"' or '')
            # icon
            if entry[1] and (not options or not options.get('no_icon')):
                html += '<img src="{icon}" alt="{label}"/> '.format(
                        icon=entry[1].format(theme=theme), label=entry[2])
            html += '<span><span>{label}</span></span>'.format(label=entry[2])
            if entry[3]:  # URL
                html += '</a>'
            html += '</span>'
            if entry[5]:  # Subentries
                html += '<ul>{0}</ul>'.format(self._xhtml_entries(
                    theme, depth + 1, entry[5], crumb_trail, options))
            html += '</li>'

        return html

    # -------------------------------------------------------------------------
    @classmethod
    def _is_current(cls, crumb_trail, entry):
        """Check if the entry has to be highlighted.

        :param listt crumb_trail:
            A trail of crumbs to compare with menu entries.
            See :meth:`.lib.breadcrumbs.Breadcrumbs.crumb_trail`.`
        :param tuple entry:
            Entry to check.
        :rtype: bool
        """
        # Compare with the current path
        if not crumb_trail:
            return False
        crumb = crumb_trail[-1]
        entry_chunks = entry[3].split('/')[1:] if entry[3] else []
        if entry_chunks[:crumb[1]] == crumb[0]:
            return True
        for subentry in entry[5] or '':
            if cls._is_current(crumb_trail, subentry):
                return True

        # Compare with the paths of the breadcrumb trail
        for crumb in crumb_trail[1:-1]:
            if entry_chunks[:crumb[1]] == crumb[0]:
                return True
        return False

    # -------------------------------------------------------------------------
    def _entry(self, piece):
        """Construct a menu entry tuple and recursively the subentries.

        :param tuple piece:
            The piece of the menu framework.
        :rtype: tuple
        :return:
            A tuple such as
            ``(class, icon, label, route_path, route, (subentry, ...))``.
        """
        subentries = []
        if piece[4] is not None:
            for subpiece in piece[4]:
                if self._has_permission(subpiece):
                    subentry = self._entry(subpiece)
                    if subentry is not None:
                        subentries.append(subentry)

        route_path = None
        if piece[3]:
            route_path = (piece[3], {}) \
                if not isinstance(piece[3], (list, tuple)) else piece[3]
            route_path = self._request.route_path(
                route_path[0], **route_path[1])

        if route_path is not None or subentries:
            return (
                make_id(piece[1], mode='class', truncate=16).lower(),
                piece[0], self._request.localizer.translate(piece[1]),
                route_path, piece[3], subentries and tuple(subentries) or None)

        return None

    # -------------------------------------------------------------------------
    def _has_permission(self, piece):
        """Check if the user has the permission to use this piece of the menu
        framework.

        :param tuple piece:
            The piece of the menu framework to check.
        :rtype: bool
        """
        if piece[2] is None:
            return True
        return self._request.has_permission(piece[2]).boolval
