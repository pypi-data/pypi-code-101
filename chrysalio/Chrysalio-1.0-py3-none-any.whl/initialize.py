"""Main class to initialize the application."""

from sys import exit as sys_exit
from os import makedirs, chdir
from os.path import exists, dirname
from shutil import rmtree
from configparser import ConfigParser
from pkg_resources import get_distribution

import transaction

from pyramid.csrf import SessionCSRFStoragePolicy

from .lib.i18n import _, add_translation_dirs, translate
from .lib.config import config_get, settings_get_list
from .lib.log import log_activity_setup
from .lib.utils import tounicode, check_chrysalio_js, check_chrysalio_css
from .lib.xml import check_chrysalio_rng
from .includes.themes import create_default_theme
from .models import get_tm_dbsession
from .models.dbsettings import DBSettings


# =============================================================================
class Initialize(object):
    """Initialization application class.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """

    # -------------------------------------------------------------------------
    def __init__(self, configurator):
        """Constructor method."""
        self._configurator = configurator

    # -------------------------------------------------------------------------
    def complete(self, global_config, package, populate_script):
        """Check settings and create registry objects.

        :param dict global_config:
            Dictionary describing the INI file with keys ``__file__`` and
            ``here``.
        :param str package:
            Name of the calling package.
        :param str populate_script:
            Name of populate script.
        """
        # Translations
        add_translation_dirs(self._configurator, package)

        # Version
        self._configurator.registry['version'] = '{0} {1}'.format(
            get_distribution(package).project_name,
            get_distribution(package).version)

        # CSRF policy
        self._configurator.set_csrf_storage_policy(
            SessionCSRFStoragePolicy())
        self._configurator.set_default_csrf_options(require_csrf=True)

        # General settings
        chdir(dirname(global_config['__file__']))
        settings = self._configurator.get_settings()
        settings['__file__'] = global_config['__file__']
        if not settings.get('site.uid'):
            sys_exit(translate(_('*** You must define a Web site ID.')))
        config = ConfigParser({'here': global_config['here']})
        config.read(tounicode(global_config['__file__']), encoding='utf8')
        default_email = config_get(config, 'Populate', 'admin.email')
        if not default_email:
            sys_exit(translate(_('*** The administrator must have an email.')))
        with transaction.manager:
            dbsession = get_tm_dbsession(
                self._configurator.registry['dbsession_factory'],
                transaction.manager)
            if 'testing' not in settings and not DBSettings.exists(dbsession):
                sys_exit(translate(
                    _('*** Run "${s}" script!', {'s': populate_script})))
            self._configurator.registry['settings'] = DBSettings.db2dict(
                settings, dbsession, default_email)

        # Theme management
        includes = settings_get_list(settings, 'chrysalio.includes')
        if 'chrysalio.includes.themes' not in includes:
            create_default_theme(self._configurator, package)

        # Create log directory
        self._configurator.registry['log_activity'] = \
            log_activity_setup(config)

        # Temporary directory
        if settings.get('temporary'):
            if exists(settings['temporary']):
                rmtree(settings['temporary'])
            makedirs(settings['temporary'])

        # Check Relax NG, Js and Css
        if package != 'chrysalio':  # pragma: nocover
            check_chrysalio_rng('{0}:RelaxNG'.format(package))
            check_chrysalio_css('{0}:Static/Css'.format(package))
            check_chrysalio_js('{0}:Static/Js'.format(package))

    # -------------------------------------------------------------------------
    def add_static_views(self, package, statics):
        """Add static views.

        :param str package:
            Name of the calling package.
        :param tuple statics:
            A tuple of tuples such as ``(static_name, static_abs_path)``.
        """
        for theme in self._configurator.registry['themes']:
            theme = '/theme/{0}'.format(theme.lower()) if theme else ''
            for static in statics:
                url = '{0}/{1}/{2}/'.format(theme, package, static[0])
                if self._configurator.introspector.get(
                        'static views', url) is None:
                    self._configurator.add_static_view(url, static[1])
