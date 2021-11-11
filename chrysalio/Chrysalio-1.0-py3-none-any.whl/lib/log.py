"""Various functions to manage logs."""

from os import makedirs
from os.path import expanduser, dirname, exists
from logging import getLogger, basicConfig
from logging.config import fileConfig
from json import loads

from .config import config_get_list

LOG_ACTIVITY = getLogger('activity')


# =============================================================================
def setup_logging(
        log_level='INFO', log_file=None, log_format=None, filemode='w'):
    """Initialize logging system.

    :param str log_level: ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
        Log level. By default `INFO`.
    :param str log_file: (optional)
        Path to log file.
    :param str log_format: (optional)
        Format for log entry. By default,
        `%(asctime)s %(levelname)-8s %(message)s`
    :param str filemode: (default='w')
        File mode: ``'w'`` or ``'a'``.
    """
    if log_format is None:
        log_format = '%(asctime)s %(levelname)-8s %(message)s'
    if log_file:
        basicConfig(
            filename=expanduser(log_file), filemode=filemode, level=log_level,
            format=log_format)
    else:
        basicConfig(level=log_level, format=log_format)


# =============================================================================
def log_activity_setup(config, config_file=None):
    """Create log directory.

    :type  config: configparser.ConfigParser
    :param config:
        Configuration of the site.
    :param str config_file:
        Absolute path to the configuration file.
    :rtype: logging.Logger
    :return:
        Return ``LOG_ACTIVITY`` if activity log is activated.
    """
    if 'activity' not in config_get_list(config, 'loggers', 'keys') or \
       not config.has_option('handler_activity', 'args'):
        return None

    # Setup logging
    if config_file is not None:  # pragma: nocover
        fileConfig(config_file, defaults={'here': dirname(config_file)})

    # Make log directory
    log_args = loads('[{0}]'.format(
        config.get('handler_activity', 'args')[1:-1]
        .replace("'", '"').replace('True', 'true') .replace('False', 'false')))
    path = dirname(log_args[0])
    if not exists(path):
        makedirs(path)

    return LOG_ACTIVITY


# =============================================================================
def log_info(request, action, *args):
    """Write an information message in the log.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str action:
        Action in action.
    :param list args:
        Non-keyworded arguments.
    """
    if request.registry.get('log_activity') is not None:
        request.registry['log_activity'].info(
            '[%s] %s %s',
            (hasattr(request, 'session') and 'user' in request.session and
             request.session['user']['login']) or
            ('context' in request.registry and
             request.registry['context'].get('login')) or '',
            action, ' '.join(args))


# =============================================================================
def log_error(request, error):
    """Write an error message in the log.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    if request.registry.get('log_activity') is not None:
        request.registry['log_activity'].error(
            '[%s] %s',
            (hasattr(request, 'session') and 'user' in request.session and
             request.session['user']['login']) or
            ('context' in request.registry and
             request.registry['context'].get('login')) or '', error)


# =============================================================================
def log_warning(request, warning):
    """Write a warning message in the log.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    if request.registry.get('log_activity') is not None:
        request.registry['log_activity'].warning(
            '[%s] %s',
            (hasattr(request, 'session') and 'user' in request.session and
             request.session['user']['login']) or
            ('context' in request.registry and
             request.registry['context'].get('login')) or '', warning)


# =============================================================================
def log_debug(request, debug):
    """Write a debug message in the log.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    if request.registry.get('log_activity') is not None:
        request.registry['log_activity'].debug(
            '[%s] %s',
            (hasattr(request, 'session') and 'user' in request.session and
             request.session['user']['login']) or
            ('context' in request.registry and
             request.registry['context'].get('login')) or '', debug)
