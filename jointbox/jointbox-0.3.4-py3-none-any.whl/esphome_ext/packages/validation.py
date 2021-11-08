#    JointBox CLI
#    Copyright (C) 2021 Dmitry Berezovsky
#    The MIT License (MIT)
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from cli_rack_validation import validate as crv
from jointbox_cli import const, validate as jb_crv
from .common import PackageConfig


def _validate_package_definition(value):
    # Shorthand - just string locator
    #   Example:
    #   packages:
    #     my_package: my_packages/package_file.yaml
    if isinstance(value, str):
        return _validate_package_source(value)
    # Legacy - using include syntax
    #   Example:
    #   packages:
    #     my_package: !include my_packages/package_file.yaml
    if isinstance(value, dict) and const.CONF_SOURCE not in value:
        return value
    # Everything else should be validated using full config schema
    return FULL_PACKAGE_SCHEMA(value)


def _validate_package_source(value):
    if isinstance(value, str):
        return crv.string_strict(value)
    if isinstance(value, dict):
        return value
    raise crv.Invalid(
        "Package should be defined either by locator string pointing the file"
        "or dictionary holding package content (deprecated)"
    )


FULL_PACKAGE_SCHEMA = crv.Schema(
    {
        crv.Required(const.CONF_SOURCE): _validate_package_source,
        crv.Optional(const.CONF_PARAMS, default={}): crv.ensure_schema({jb_crv.valid_param_name: crv.anything}),
    }
)
PACKAGE_DEFINITION_SCHEMA = crv.Schema(_validate_package_definition)


def _validate_package_config(package_name: str, package_config: PackageConfig) -> PackageConfig:
    """
    There are 2 versions of the syntax supported.
    The short one: Either dictionary representing package source or string locator pointing
                   the package file or directory
    The regular one: dictionary of the following structure
                     source: dict or string - required, dictionary representing package source
                     params: dict           - optional, key-value params to be added to expression
                                                        evaluator scope for this package.
                                                        Value could be any type supported by YAML
    :param package_name:    name of the package to be validated
    :param package_config:  package configuration to be validated
    :return: None
    :raises: cv.Invalid - in case when configuration is invalid
    """
    return PACKAGE_DEFINITION_SCHEMA(package_config)


def _is_short_package_config_syntax(package_config: PackageConfig) -> bool:
    if isinstance(package_config, str):
        return True
    if isinstance(package_config, dict):
        return const.CONF_SOURCE not in package_config.keys()
    return False
