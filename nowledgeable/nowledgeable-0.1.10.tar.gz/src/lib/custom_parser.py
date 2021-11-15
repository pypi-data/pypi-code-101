#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""

Generic Arg Parser wrapping Argparse class

"""


#TODO: Global CLI Utils

import argparse
import ctypes
import locale
import os
import sys
import re

#TODO: Text wrapping in argparser

VERSION = 1.0

supported_lang = ["en", "fr"]

base_texts = {
    "usage": {
        "fr": "Utilisation:",
        "en": "Usage:"
    },

    "version": {
        "fr": "Montrer la version du programme et finir l'exécution",
        "en": "Show program's version number and exit the program"
    },

    "help": {
        "fr": "Montrer ce message d'aide et finir l'exécution",
        "en": "Show this help message and exit the program"
    },

    "optional_args": {
        "fr": "Arguments optionnels",
        "en": "Optional arguments"
    },

    "positional_args": {
        "fr": "Argument positionnels",
        "en": "Positional arguments"
    },

    "no_description": {
        "fr": "<Pas de description>",
        "en": "<No description>"
    }
}


def get_os_language():
    if os.name != 'posix':
        windll = ctypes.windll.kernel32
        lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]
    else:
        lang = os.environ['LANG']

    return lang


def raise_(e):
    raise e


def RegexType(pat):
    if type(pat) == str:
        pat = re.compile(pat)

    return lambda arg: arg if pat.match(arg) else raise_(argparse.ArgumentTypeError)


def create_help_formatter(lang):
    class CapitalisedHelpFormatter(argparse.RawTextHelpFormatter):
        def add_usage(self, usage, actions, groups, prefix=None):
            if prefix is None:
                prefix = "{} ".format(base_texts["usage"][lang])
            return super(CapitalisedHelpFormatter, self).add_usage(
                usage, actions, groups, prefix)

    return CapitalisedHelpFormatter

def get_first(_dict, keys, default=None):
    for key in keys:
        if key in _dict:
            return _dict[key]

    return default


def get_subdict(_dict, subkey, keys, default):
    if subkey in _dict:
        val = get_first(_dict[subkey], keys)
    else:
        val = None

    return val if val != None else default

class CustomParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('Error: %s\n\n' % message.capitalize())
        self.print_help()
        sys.exit(1)

def create_custom_parser(description_texts, prog=None, version_string=None):
    lang = get_os_language()[:2]
    default_lang = "en"

    if lang not in supported_lang:
        lang = default_lang

    desc = get_subdict(description_texts, "main_description", (lang, default_lang), get_first(
        base_texts["no_description"], (lang, default_lang)))
    if prog != None:
        parser = CustomParser(
            add_help=False,
            description=desc,
            prog=prog,
            formatter_class=create_help_formatter(lang)
        )

        version_string = version_string if version_string != None else "{}: Unknown ver. - Custom Parser v{}".format(
            prog, VERSION)

    else:
        parser = CustomParser(
            add_help=False,
            description=desc,
            formatter_class=create_help_formatter(lang)
        )

        version_string = version_string if version_string != None else "CLI: Unknown ver. - Custom Parser v{}".format(
            VERSION)

    parser.add_argument('-v', '--version', action='version',
                        version=version_string, help=get_first(base_texts["version"], (lang, default_lang)))
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help=get_first(base_texts["help"], (lang, default_lang)))

    parser._positionals.title = get_first(
        base_texts["positional_args"], (lang, default_lang))
    parser._optionals.title = get_first(
        base_texts["optional_args"], (lang, default_lang))

    return parser, lang
