# -*- coding: utf-8 -*-
"""Breadcrumbs utility."""

from webhelpers2.html import literal

from .i18n import _


DEFAULT_ROOT_CHUNKS = 20


# =============================================================================
class Breadcrumbs(object):
    """User breadcrumb trail, current title page and back URL management.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str sep: (optional)
        Separator for brundcrumb trail.

    This class uses session and stores its history in
    ``session['breadcrumbs']``. It is a list of crumbs. Each crumb is a tuple
    such as ``(title, route_name, route_params, chunks_to_compare)``.
    """

    # -------------------------------------------------------------------------
    def __init__(self, request, sep=' ‣ '):
        """Constructor method."""
        self._request = request
        self._sep = sep

    # -------------------------------------------------------------------------
    def __call__(self, title, length=10, root_chunks=DEFAULT_ROOT_CHUNKS,
                 replace=None, anchor=None, forced_route=None,
                 compare_params=False):
        """Add a crumb in breadcrumb trail.

        :param str title:
            Current page title.
        :param int length: (default=10)
            Maximum crumb number. If 0, it keeps the current length.
        :param int root_chunks: (default=20)
            Number of route path chunks to compare to highlight a menu entry.
        :param str replace: (optional):
            If current path is ``replace``, this method call :meth:`pop` before
            any action.
        :param str anchor: (optional)
            Anchor to add.
        :param tuple forced_route: (optional)
            A tuple such as ``(route_name, route_params)`` to force the route.
        :param bool compare_params: (default=False)
            If ``True`` use route parameters to differentiate the current route
            from those currently in breadcrumbs.
        """
        # pylint: disable = too-many-arguments
        # Environment
        session = self._request.session
        if 'breadcrumbs' not in session:
            session['breadcrumbs'] = []
        if not length:
            length = len(session['breadcrumbs'])

        # Replace
        if replace and self.current_path() == replace:
            self.pop()

        # Scan old breadcrumb trail to find the right position
        route_name = (forced_route and forced_route[0]) or \
            (self._request.matched_route and self._request.matched_route.name)
        if route_name is None:
            session['breadcrumbs'].append((title, None, {}, root_chunks))
            return
        params = self._request.matchdict if forced_route is None \
            else forced_route[1]
        crumbs = []
        for crumb in session['breadcrumbs']:
            if len(crumbs) >= length - 1 \
               or (crumb[1] == route_name and not compare_params) \
               or (crumb[1] == route_name and crumb[2] == params):
                break
            crumbs.append(crumb)

        # Add new breadcrumb
        if anchor is not None:
            params['_anchor'] = anchor
        crumbs.append((title, route_name, params, root_chunks))
        session['breadcrumbs'] = crumbs

    # -------------------------------------------------------------------------
    def pop(self):
        """Pop last breadcrumb."""
        session = self._request.session
        if 'breadcrumbs' in session and len(session['breadcrumbs']) > 1:
            session['breadcrumbs'] = session['breadcrumbs'][0:-1]

    # -------------------------------------------------------------------------
    def trail(self):
        """Output XHTML breadcrumb trail.

        :rtype: str
        """
        if 'breadcrumbs' not in self._request.session \
           or len(self._request.session['breadcrumbs']) < 2:
            return literal('&nbsp;')

        translate = self._request.localizer.translate
        crumbs = []
        for crumb in self._request.session['breadcrumbs'][0:-1]:
            if crumb[1] is not None:
                crumbs.append('<a href="{path}">{label}</a>'.format(
                    path=self._request.route_path(crumb[1], **crumb[2]),
                    label=translate(crumb[0])))
            else:
                crumbs.append(translate(crumb[0]))
        crumbs.append(translate(self._request.session['breadcrumbs'][-1][0]))
        return literal(self._sep.join(crumbs))

    # -------------------------------------------------------------------------
    def crumb_trail(self):
        """Return a trail of crumbs to compare with menu entries. Each crumb
        is tuple of a list of path chunks and a comparison length.

        :rtype: list
        :return:
            A list of crumbs. Each crumb is a tuple such as
            ``([chunk1, chunk2,...], root_chunks)`` where ``root_chunks`` is a
            number of route path chunks to compare to highlight a menu entry
        """
        if self._request.matched_route is None:
            return []
        current = (
            self._request.current_route_path().partition('?')[0].split('/')[
                1:DEFAULT_ROOT_CHUNKS + 1], DEFAULT_ROOT_CHUNKS)
        if 'breadcrumbs' not in self._request.session:
            return [current]

        crumbs = []
        for crumb in self._request.session['breadcrumbs']:
            if crumb[1] is not None:
                path = self._request.route_path(
                    crumb[1], **crumb[2]).split('/')
                crumbs.append((path[1:crumb[3] + 1], crumb[3]))
        if not crumbs or crumbs[-1][0] != current[0]:
            crumbs.append(current)
        return crumbs

    # -------------------------------------------------------------------------
    def current_title(self):
        """Title of current page.

        :rtype: str
        """
        if 'breadcrumbs' not in self._request.session \
           or not self._request.session['breadcrumbs'] \
           or not self._request.session['breadcrumbs'][-1][1]:
            return self._request.localizer.translate(_('Home'))
        return self._request.localizer.translate(
            self._request.session['breadcrumbs'][-1][0])

    # -------------------------------------------------------------------------
    def current_route_name(self):
        """Route name of current page.

        :rtype: str
        """
        if 'breadcrumbs' not in self._request.session \
           or not self._request.session['breadcrumbs'] \
           or not self._request.session['breadcrumbs'][-1][1]:
            return 'home'
        return self._request.session['breadcrumbs'][-1][1]

    # -------------------------------------------------------------------------
    def current_path(self):
        """Path of current page.

        :rtype: str
        """
        if 'breadcrumbs' not in self._request.session \
           or not self._request.session['breadcrumbs'] \
           or not self._request.session['breadcrumbs'][-1][1]:
            return self._request.route_path('home')
        return self._request.route_path(
            self._request.session['breadcrumbs'][-1][1],
            **self._request.session['breadcrumbs'][-1][2])

    # -------------------------------------------------------------------------
    def back_title(self):
        """Output title of previous page.

        :rtype: str
        """
        if 'breadcrumbs' not in self._request.session \
           or len(self._request.session['breadcrumbs']) < 2 \
           or not self._request.session['breadcrumbs'][-2][1]:
            return self._request.localizer.translate(_('Home'))
        return self._request.localizer.translate(
            self._request.session['breadcrumbs'][-2][0])

    # -------------------------------------------------------------------------
    def back_path(self):
        """Output the path of previous page.

        :rtype: str
        """
        if 'breadcrumbs' not in self._request.session \
           or len(self._request.session['breadcrumbs']) < 2 \
           or not self._request.session['breadcrumbs'][-2][1]:
            return self._request.route_path('home')
        return self._request.route_path(
            self._request.session['breadcrumbs'][-2][1],
            **self._request.session['breadcrumbs'][-2][2])
