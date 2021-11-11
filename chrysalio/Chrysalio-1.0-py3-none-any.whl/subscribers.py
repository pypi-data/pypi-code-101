"""Subscriber definition."""

from os.path import splitext

from pyramid.events import BeforeRender
from pyramid.threadlocal import get_current_request
from pyramid.i18n import TranslationString

from .lib.utils import tostr, camel_case
from .lib.breadcrumbs import Breadcrumbs
from .lib.panel import Panel
from .includes.themes import theme_template, theme_static_prefix
from .includes.themes import theme_has_static


# =============================================================================
def includeme(configurator):
    """Function to include subscribers.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    configurator.add_subscriber(before_render, BeforeRender)
    configurator.add_request_method(Breadcrumbs, 'breadcrumbs', reify=True)


# =============================================================================
def before_render(event):
    """A subscriber for :class:`pyramid.events.BeforeRender` events.

    :type  event: pyramid.events.BeforeRender
    :param event:
        Current event.
    """
    request = event.get('request') or get_current_request()
    domain = event.get('renderer_name', '')
    domain = domain.partition(':')[0] if ':' in domain else 'chrysalio'

    def translate(text, mapping=None, domain=domain):
        """Translation from a string."""
        return request.localizer.translate(TranslationString(
            text, mapping=mapping, domain=domain))

    event['_'] = translate
    event['route'] = lambda name, *elts, **kwargs: \
        tostr(request.route_path(name, *elts, **kwargs))
    event['title'] = request.registry['settings']['title']
    event['page_id'] = camel_case(
        splitext(event.get('renderer_name', '').split('/')[-1:][0])[0])
    event['theme'] = theme_static_prefix(request)
    event['theme_has'] = theme_has_static
    event['panel_css'] = Panel.open_panel_css(request)
    event['panel_js'] = Panel.open_panel_js(request)
    event['layout'] = theme_template(request, 'layout')
