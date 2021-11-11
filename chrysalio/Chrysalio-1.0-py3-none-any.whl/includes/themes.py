"""Theme management."""

from sys import exit as sys_exit
from os.path import exists, join, abspath
from configparser import ConfigParser

from pyramid.asset import abspath_from_asset_spec
from pyramid.config import Configurator

from ..lib.i18n import _, translate
from ..lib.config import config_get_namespace
from ..lib.config import settings_get_list, settings_get_directories


# =============================================================================
def includeme(configurator):
    """Function to include themes.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    if isinstance(configurator, Configurator):
        load_themes(configurator)


# =============================================================================
def load_themes(configurator):
    """Load available themes in registry.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.

    Set into registry a tuple such as ``(default_theme, theme_dict)`` where
    ``theme_dict`` is a dictionary like ``{'theme_id': theme_info,...}``.
    ``theme_info`` is a dictionary with keys ``path``, ``layout``,
    ``login``,...
    """
    # Read list of available themes
    themes = {}
    directories = settings_get_directories(
        configurator.get_settings(), 'theme', 'theme.conf')
    for theme_id, dir_path in directories.items():
        config = ConfigParser({'here': dir_path})
        config.read(join(dir_path, 'theme.conf'), encoding='utf8')
        themes[theme_id] = {
            'path': dir_path,
            'name': config_get_namespace(config, 'Description', 'name')}
        for section in ('Templates', 'Static'):
            if not config.has_section(section):
                sys_exit(translate(_(
                    '*** Theme "${t}" must have a section [${s}].',
                    {'t': theme_id, 's': section})))
            if section == 'Templates' and \
                    not config.has_option(section, 'layout'):
                sys_exit(translate(_(
                    '*** An option is missing for [${s}] of theme "${t}".',
                    {'s': section, 't': theme_id})))
            if section == 'Static' and (
                    not config.has_option(section, 'css') or
                    not config.has_option(section, 'js')):
                sys_exit(translate(_(
                    '*** An option is missing for [${s}] of theme "${t}".',
                    {'s': section, 't': theme_id})))
            for item in config.items(section):
                if item[0] == 'here':
                    continue
                if not item[1]:
                    sys_exit(translate(_(
                        '*** Option "${o}" of theme "${t}" must be defined.',
                        {'o': item[0], 't': theme_id})))
                path = abspath(abspath_from_asset_spec(item[1]))
                if not exists(path):
                    sys_exit(translate(_(
                        '*** File "${f}" of theme "${t}" does not exist.',
                        {'f': path, 't': theme_id})))
                if section == 'Templates':
                    themes[theme_id][item[0]] = path
                else:
                    configurator.add_static_view(
                        '/theme/{theme_id}/{static_id}/'.format(
                            theme_id=theme_id.lower(), static_id=item[0]),
                        path)
    configurator.registry['themes'] = themes
    configurator.commit()

    # Read default theme
    default = configurator.registry['settings']['theme']
    default = settings_get_list(
        configurator.get_settings(), 'theme.patterns', [''])[0] \
        if not default and default not in themes and themes else default
    if default not in themes:
        sys_exit(translate(_('*** Must have an existing default theme.')))
    configurator.registry['settings']['theme'] = default


# =============================================================================
def create_default_theme(configurator, package):
    """If the theme management is not activated, it creates a default theme in
    registry.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    :param str package:
        Name of the calling package.
    """
    # Templates
    settings = configurator.get_settings()
    path = abspath(abspath_from_asset_spec('{0}:Templates'.format(package)))
    configurator.registry['themes'] = {
        '': {'path': None, 'name': {},
             'layout': settings.get('site.layout', join(path, 'layout.pt'))}}

    # Static
    path = abspath(abspath_from_asset_spec('{0}:Static'.format(package)))

    configurator.add_static_view(
        '/css/', settings.get('site.css', join(path, 'Css')))
    configurator.add_static_view(
        '/js/', settings.get('site.js', join(path, 'Js')))
    configurator.add_static_view(
        '/images/', settings.get('site.images', join(path, 'Images')))
    configurator.add_static_view(
        '/custom/', settings.get('site.custom', join(path, 'Custom')))

    configurator.commit()


# =============================================================================
def theme_template(request, template_id):
    """Retrieve the absolute file path of the file ``template_id`` of the
    current theme.

    :param request: pyramid.request.Request`
    :param request:
        Current request.
    :param str template_id:
        ID of the file to retrieve.
    :rtype: str
    :return:
        Absolute path to the template file or ``None``.
    """
    theme_id = request.session.get(
        'theme', request.registry['settings']['theme'])
    return request.registry['themes'][theme_id].get(template_id)


# =============================================================================
def theme_static_prefix(request):
    """Return the URL prefix for the current theme.

    :param request: pyramid.request.Request`
    :param request:
        Current request.
    :rtype: str
        A string such as ``/theme/alternative`` for theme `Alternative` or ''.
    """
    if request is None:
        return ''
    theme_id = request.session.get(
        'theme', request.registry['settings']['theme'])
    return '/theme/{0}'.format(theme_id.lower()) if theme_id else ''


# =============================================================================
def theme_has_static(request, static_id):
    """Return ``True`` if the descriminator exists in static views.

    :param request: pyramid.request.Request`
    :param request:
        Current request.
    :param str static_id:
        ID of static view to check.
    :rtype: bool
    """
    theme_id = request.session.get(
        'theme', request.registry['settings']['theme'])
    return request.registry.introspector.get(
        'static views', '/theme/{theme_id}/{static_id}/'.format(
            theme_id=theme_id.lower(), static_id=static_id)) is not None
