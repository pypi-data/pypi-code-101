from uip.utils import generic
import os

login_options = {
    'userid': {'short_arg': '-u', 'long_arg': '--userid', 'env_var': 'UIP_USERID', 'config_arg': 'userid',
               'default': None},
    'password': {'short_arg': '-w', 'long_arg': '--password', 'env_var': 'UIP_PASSWORD', 'config_arg': None,
                 'default': None},
    'url': {'short_arg': '-i', 'long_arg': '--url', 'env_var': 'UIP_URL', 'config_arg': 'url', 'default': None},
}

config_options = {
    'shared': {
        # options that are shared across the various commands
    },
    'init': {
        'extension_template': {'short_arg': '-t', 'long_arg': '--extension-template', 'env_var': None,
                               'config_arg': None, 'default': None},
        'variables': {'short_arg': '-e', 'long_arg': '--variables', 'env_var': 'UIP_TEMPLATE_VARIABLES',
                      'config_arg': 'variables', 'default': None},
        'dir': {'default': os.getcwd()}
    },
    'build': {
        'all': {'short_arg': '-a', 'long_arg': '--all', 'env_var': 'UIP_BUILD_ALL', 'config_arg': 'build-all',
                'default': False}
    },
    'upload': {
        'all': {'short_arg': '-a', 'long_arg': '--all', 'env_var': 'UIP_UPLOAD_ALL', 'config_arg': 'upload-all',
                'default': False},
    },
    'push': {
        'all': {'short_arg': '-a', 'long_arg': '--all', 'env_var': 'UIP_PUSH_ALL', 'config_arg': 'push-all',
                'default': False},
    },
    'pull': {
    },
    'download': {
        'template_name': {'short_arg': '-n', 'long_arg': '--template-name', 'env_var': 'UIP_TEMPLATE_NAME',
                          'config_arg': 'template-name', 'default': None},
    }
}

for config_option in ['shared', 'upload', 'push', 'pull', 'download']:
    config_options[config_option].update(login_options)


def get_config_options_dict():
    return generic.deep_copy_dict(config_options)


def get_value(option, attribute):
    option_dest = option.split('.')

    value = get_config_options_dict()
    for dest in option_dest:
        value = value.get(dest, {})

    return value.get(attribute, None)


def get_short_arg(option):
    return get_value(option, 'short_arg')


def get_long_arg(option):
    return get_value(option, 'long_arg')


def get_env_var_name(option):
    return get_value(option, 'env_var')


def get_config_arg(option):
    return get_value(option, 'config_arg')


def get_default_value(option):
    return get_value(option, 'default')
