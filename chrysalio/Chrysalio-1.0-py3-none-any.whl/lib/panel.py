"""Panel class."""

from webhelpers2.html import literal
from chameleon import PageTemplateFile

from pyramid.asset import abspath_from_asset_spec

from chrysalio.lib.utils import tostr
from chrysalio.lib.form import get_action, Form
from ..includes.themes import theme_static_prefix
from .i18n import _


PANEL_ITEM_PREFIX = 'panel:'


# =============================================================================
class Panel(object):
    """Class to manage side panel.

    :param list area: (optional)
        List of route names which determine the area where the panel is
        visible.
    """

    uid = None
    label = None
    icon = '/images/panel.png'
    template = 'chrysalio:Templates/panel.pt'
    css = ()
    javascripts = ()
    constants = {}
    need_form = False

    # -------------------------------------------------------------------------
    def __init__(self, area=None):
        """Constructor method."""
        self.area = area or ()

    # -------------------------------------------------------------------------
    @classmethod
    def register(cls, registry, panel_class, area=None, add2systray=True):
        """Method to register the panel and possibly add it to the panel
        systray.

        :type  registry: pyramid.registry.Registry
        :param registry:
            Application registry.
        :param panel_class:
            Panel class.
        :param list area: (optional)
            List of route names which determine the area where the panel is
            visible.
        :param bool add2systray: (default=True)
            If ``True`` add the panel to systray.
        :rtype: :class:`.lib.panel.Panel` or ``None``
        """
        if panel_class.uid is None or panel_class.label is None:
            return None
        if 'panels' not in registry:
            registry['panels'] = {}
        if panel_class.uid in registry['panels']:
            return registry['panels'][panel_class.uid]
        registry['panels'][panel_class.uid] = panel_class(area)

        if add2systray:
            if 'systray' not in registry:
                registry['systray'] = []
            registry['systray'].append(registry['panels'][panel_class.uid])

        return registry['panels'][panel_class.uid]

    # -------------------------------------------------------------------------
    @classmethod
    def has_open_panel(cls, request):
        """Return ``'cioHasOpenPanel'`` if almost one panel is open.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: class:`str` or ``None``
        """
        if 'panels' not in request.registry or 'panels' not in request.session:
            return None
        for panel in request.registry['panels'].values():
            if panel.uid in request.session['panels'] and \
               request.session['panels'][panel.uid]['is_open']:
                return 'cioHasOpenPanel'
        return None

    # -------------------------------------------------------------------------
    def is_open(self, request):
        """``True`` if the panel is open.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        self._prepare_session(request)
        if self.area and (
                request.matched_route is None or
                request.matched_route.name not in self.area):
            self.close(request)
        return request.session['panels'][self.uid]['is_open']

    # -------------------------------------------------------------------------
    def was_open(self, request):
        """``True`` if the panel was previously open.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        self._prepare_session(request)
        return request.session['panels'][self.uid]['was_open']

    # -------------------------------------------------------------------------
    def open(self, request):
        """Open the panel and memorize the state.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        self._prepare_session(request)
        request.session['panels'][self.uid]['was_open'] = self.is_open(request)
        request.session['panels'][self.uid]['is_open'] = True

        if 'panels' in request.registry:
            for other in request.registry['panels'].values():
                if other.uid != self.uid:
                    other.close(request)

    # -------------------------------------------------------------------------
    def close(self, request):
        """Close the panel and memorize the state.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        self._prepare_session(request)
        request.session['panels'][self.uid]['was_open'] = False
        request.session['panels'][self.uid]['is_open'] = False

    # -------------------------------------------------------------------------
    def clear_values(self, request):
        """Clear all values of this panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        if 'panels' in request.session \
           and self.uid in request.session['panels'] \
           and 'values' in request.session['panels'][self.uid]:
            del request.session['panels'][self.uid]['values']

    # -------------------------------------------------------------------------
    def set_values(self, request, values):
        """Set values of this panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param dict values:
            Values to set.
        """
        self._prepare_session(request)
        request.session['panels'][self.uid]['values'] = values

    # -------------------------------------------------------------------------
    def values(self, request):
        """Return values of this panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: dict
        """
        self._prepare_session(request)
        return request.session['panels'][self.uid].get('values', {})

    # -------------------------------------------------------------------------
    def set_value(self, request, value_id, value):
        """Set a value of this panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str value_id:
            Value ID.
        :param value:
            Value to set.
        """
        self._prepare_session(request)
        if 'values' not in request.session['panels'][self.uid]:
            request.session['panels'][self.uid]['values'] = {}
        request.session['panels'][self.uid]['values'][value_id] = value

    # -------------------------------------------------------------------------
    def value(self, request, value_id):
        """Return the value ``value_id`` of this panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str value_id:
            ID of the requested value.
        :rtype: str
        """
        return self.values(request).get(value_id)

    # -------------------------------------------------------------------------
    def render(self, request, ts_factory=_):
        """Return the content of the panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param ts_factory: (default=_)
            Translation String Factory fucntion.
        :rtype: webhelpers2.html.literal
        """
        domain = self.template.partition(':')[0] \
            if ':' in self.template else 'chrysalio'

        def _translate(
                msgid, domain=domain, mapping=None, target_language=None):
            """Translation for Chameleon."""
            # pylint: disable = unused-argument
            return request.localizer.translate(
                msgid, domain=domain, mapping=mapping)

        params = {
            'request': request,
            '_':  ts_factory,
            'route': lambda name, *elts, **kwargs: tostr(
                request.route_path(name, *elts, **kwargs)),
            'theme': theme_static_prefix(request),
            'get_action': lambda request: get_action(request, True),
            'PANEL_ITEM_PREFIX': PANEL_ITEM_PREFIX,
            'panel': self}
        params.update(self.constants)
        params.update(self.values(request))
        if self.need_form:
            params['form'] = Form(
                request, defaults=params.get('form_defaults'),
                force_defaults='form_defaults' in params)
            params['form'].forget(PANEL_ITEM_PREFIX)

        return literal(PageTemplateFile(
            abspath_from_asset_spec(self.template),
            translate=_translate).render(**params))

    # -------------------------------------------------------------------------
    def route(self, request):
        """Return the route to toggle the state of the panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: str
        """
        if 'panel' in request.GET:
            del request.GET['panel']
        query_string = dict(request.GET)
        query_string.update({'panel': self.uid})
        if request.matched_route is None:
            self.close(request)
            return ''
        return request.current_route_path(_query=query_string)

    # -------------------------------------------------------------------------
    @classmethod
    def open_panel_css(cls, request):
        """Return a list of URL of CSS used by the open panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: tuple
        """
        for panel in request.registry.get('panels', {}).values():
            if panel.is_open(request):
                return panel.css

        return ()

    # -------------------------------------------------------------------------
    @classmethod
    def open_panel_js(cls, request):
        """Return a list of URL of Javascript used by the open panel.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: tuple
        """
        for panel in request.registry.get('panels', {}).values():
            if panel.is_open(request):
                return panel.javascripts

        return ()

    # -------------------------------------------------------------------------
    @classmethod
    def manage_panels(cls, request):
        """Possibly, toggle the current panel state.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        if 'panels' not in request.registry:
            return

        # Was open
        for panel in request.registry['panels'].values():
            if panel.is_open(request):
                request.session['panels'][panel.uid]['was_open'] = True

        # Close or open a panel
        panel_id = request.GET.get('panel')
        if panel_id and panel_id in request.registry['panels']:
            panel = request.registry['panels'][panel_id]
            if panel.is_open(request):
                panel.close(request)
            else:
                panel.open(request)

    # -------------------------------------------------------------------------
    def _prepare_session(self, request):
        """Prepare session to memorize panel state.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """
        if 'panels' not in request.session:
            request.session['panels'] = {}
        if self.uid not in request.session['panels']:
            request.session['panels'][self.uid] = {
                'was_open': False, 'is_open': False}
