"""Various functions to parse configuration files or settings."""

try:  # pragma: nocover
    from os import scandir
except ImportError:  # pragma: nocover
    from scandir import scandir
from os.path import exists, join, abspath
from sys import version_info
from fnmatch import fnmatch

from pyramid.asset import abspath_from_asset_spec
from pyramid.security import Allow


# =============================================================================
def update_acl(configurator, principals):
    """Update root factory Access Control List (ACL) with permissions.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    :param tuple principals:

    ``principals`` is a tuple such as::

        DOCUMENT_PRINCIPALS = (
            ('document', _('Document management'), (
                ('viewer', _('View all documents'), (
                    'document-view',)),
                ('editor', _('Edit any document'), (
                    'document-view', 'document-edit'))
            )),
        )
    """
    root_factory = configurator.introspector.get(
        'root factories', None).get('factory')
    root_factory.__acl__ += [
        (Allow, '{0}.{1}'.format(group[0], principal[0]), principal[2])
        for group in principals for principal in group[2]]


# =============================================================================
def config_get(config, section, option, default=None):
    """Retrieve a value from a configuration object.

    :type  config: configparser.ConfigParser
    :param config:
        Configuration object.
    :param str section:
        Section name.
    :param str option:
        Option name.
    :param str default: (optional)
        Default value
    :rtype: str
        Read value or default value.
    """
    if not config.has_option(section, option):
        return default
    value = config.get(section, option)
    if version_info > (3, 0):
        return value or None  # pragma: no cover
    return value.decode('utf8') if isinstance(value, str) \
        else value  # pragma: no cover


# =============================================================================
def config_get_list(config, section, option, default=None):
    """Retrieve a list of values from a configuration object.

    :type  config: configparser.ConfigParser
    :param config:
        Configuration object.
    :param str section:
        Section name.
    :param str option:
        Option name.
    :param list default: (optional)
        Default values.
    :rtype: list
    """
    if not config.has_option(section, option):
        return default or []
    values = config_get(config, section, option)
    return [k.strip() for k in values.split(',') if k] if values else []


# =============================================================================
def config_get_namespace(config, section, namespace):
    """Retrieve all options beginning by a name space.

    :type  config: configparser.ConfigParser
    :param config:
        Configuration object.
    :param str section:
        Section name.
    :param str namespace:
        Prefix of options to retrieve.
    :rtype: dict
    """
    values = {}
    ns_len = len(namespace) + 1
    if not config.has_section(section):
        return values

    for option in config.options(section):
        if option.startswith('{0}.'.format(namespace)):
            values[option[ns_len:].replace('.', '_')] = config_get(
                config, section, option)
    return values


# =============================================================================
def settings_get_list(settings, option, default=None):
    """Retrieve a list of values from a settings dictionary.

    :type  settings: pyramid.registry.Registry.settings
    :param settings:
        Settings object.
    :param str option:
        Option name.
    :param list default: (optional)
        Default values.
    :rtype: list
    """
    if not settings.get(option):
        return default or []
    return [k.strip() for k in settings[option].split(',') if k]


# =============================================================================
def settings_get_namespace(settings, namespace):
    """Retrieve all options beginning by a name space.

    :type  settings: pyramid.registry.Registry.settings
    :param settings:
        Settings object.
    :param str namespace:
        Prefix of options to retrieve.
    :rtype: dict
    """
    values = {}
    ns_len = len(namespace) + 1

    for option in settings:
        if option.startswith('{0}.'.format(namespace)):
            values[option[ns_len:].replace('.', '_')] = settings[option]
    return values


# =============================================================================
def settings_get_directories(settings, namespace, conf_file):
    """Retrieve all directories whose root is contained in one of the
    directories listed in ``namespace.roots``, name matches one of the patterns
    listed in ``namespace.patterns`` and containing the file ``filename``.

    :type  settings: pyramid.registry.Registry.settings
    :param settings:
        Settings object.
    :param str namespace:
        Prefix of options to retrieve.
    :param str namespace:
        Prefix of options to retrieve.
    :param str conf_file:
        Name of configuration file to search in each directory.
    :rtype: dict
    """
    directories = {}
    done = set()
    patterns = settings_get_list(
        settings, '{0}.patterns'.format(namespace), '')
    for root in settings_get_list(
            settings, '{0}.roots'.format(namespace), ''):
        root = abspath(abspath_from_asset_spec(root))
        if root in done or not exists(root):
            continue
        for entry in scandir(root):
            if entry.is_dir() and exists(join(entry.path, conf_file)):
                for pattern in patterns:
                    if fnmatch(entry.name, pattern):
                        directories[entry.name] = entry.path
                        break

    return directories
