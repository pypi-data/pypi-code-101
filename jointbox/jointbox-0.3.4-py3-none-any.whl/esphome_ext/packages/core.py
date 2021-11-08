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

import copy
import logging
import os
from collections import defaultdict
from typing import Optional, Dict, Any

from cli_rack.loader import LoadedDataMeta, DefaultLoaderRegistry, LoaderRegistry
from cli_rack.utils import none_throws, safe_cast

from cli_rack_validation import crv
from .const import CONTEXT_PKG, CONTEXT_VARS, CONTEXT_MACROS, CONTEXT_META, CONTEXT_PACKAGES
from .validation import _validate_package_config, _is_short_package_config_syntax
from .common import PackageDefinition, PackageConfig, PackageSource, PackageMeta, MacroDef, BaseMeta, RootMeta
from ..expressions import register_global
from ..expressions.core import ExpressionEvaluator
from ... import const
from ...const import CONTEXT_SECRETS
from ...core import load_yaml_config_file
from ...validate import (
    valid_params_def,
    ParameterValidators,
    valid_id,
    valid_param_name,
    ensure_valid_export_def,
    valid_macros_def,
)

_LOGGER = logging.getLogger("esp.pkg")


def _merge_package(full_old, full_new):
    def merge_lists(l1: list, l2: list):
        try:
            d: Dict = defaultdict(dict)
            for x in (l1, l2):
                for elem in x:
                    d[elem["id"]].update(elem)
            return list(d.values())
        except Exception:
            return l1 + l2

    def merge(old, new):
        # pylint: disable=no-else-return
        if isinstance(new, dict):
            if not isinstance(old, dict):
                return new
            res = old.copy()
            for k, v in new.items():
                res[k] = merge(old[k], v) if k in old else v
            return res
        elif isinstance(new, list):
            if not isinstance(old, list):
                return new
            return merge_lists(old, new)

        return new

    return merge(full_old, full_new)


class PackageExpressionEvaluator(ExpressionEvaluator):
    def __init__(self, package: Optional[PackageDefinition] = None) -> None:
        super().__init__()
        self.package = package
        self.refresh_context()

    def copy(self) -> "PackageExpressionEvaluator":
        inst = safe_cast(PackageExpressionEvaluator, super().copy())
        inst.package = self.package
        return inst

    def refresh_context(self):
        if self.package is not None:
            self.local_context.clear()
            self.local_context.update(self._create_context_for_package())

    def _create_context_for_package(self) -> dict:
        if self.package is None:
            return {}
        return {
            CONTEXT_PKG: self.package,
            CONTEXT_VARS: self.package.meta.variables,
        }


class RootExpressionEvaluator(PackageExpressionEvaluator):
    def __init__(self, package: Optional[PackageDefinition] = None, secrets: Dict[str, Any] = None) -> None:
        self.secrets = secrets
        super().__init__(package)

    def _create_context_for_package(self) -> dict:
        if self.package is None:
            return {}
        return {
            CONTEXT_META: self.package,
            CONTEXT_MACROS: self.package.macros,
            CONTEXT_VARS: self.package.meta.variables,
            CONTEXT_PACKAGES: self.package.packages,
            CONTEXT_SECRETS: self.secrets,
        }


class PackageMetaReader:
    META_SCHEMA = crv.Schema(
        {
            const.CONF_DESCRIPTION: crv.string_strict,
            const.CONF_AUTHOR: crv.ensure_email_dict,
            const.CONF_TAGS: crv.ensure_list(crv.string),
            const.CONF_LICENSE: crv.string,
            const.CONF_PARAMS: valid_params_def,
            const.CONF_VARIABLES: {valid_param_name: crv.anything},
            const.CONF_EXPORT: crv.ensure_list(ensure_valid_export_def),
            const.CONF_MACROS: valid_macros_def,
        }
    )
    ROOT_META_SCHEMA = crv.Schema(
        {
            const.CONF_DESCRIPTION: crv.string_strict,
            const.CONF_AUTHOR: crv.ensure_email_dict,
            const.CONF_TAGS: crv.ensure_list(crv.string),
            const.CONF_LICENSE: crv.string,
            const.CONF_VARIABLES: {valid_param_name: crv.anything},
            const.CONF_MACROS: valid_macros_def,
        }
    )

    @classmethod
    def parse_common(cls, meta: BaseMeta, meta_dict: dict, package: PackageDefinition):
        meta.name = meta_dict.get(const.CONF_NAME)
        meta.tags = meta_dict.get(const.CONF_TAGS, [])
        meta.license = meta_dict.get(const.CONF_LICENSE)
        meta.description = meta_dict.get(const.CONF_DESCRIPTION)
        meta.variables = meta_dict.get(const.CONF_VARIABLES, {})

    @classmethod
    def _process_macros(cls, meta: BaseMeta, meta_dict: dict, package: PackageDefinition):
        macros_dict: Dict[str, Dict[str, Any]] = meta_dict.get(const.CONF_MACROS, {})
        if len(macros_dict) > 0:
            for name, macro_d in macros_dict.items():
                macro = MacroDef(name, package)
                macro.params_def = macro_d.get(const.CONF_PARAMS, {})
                macro.description = macro_d.get(const.CONF_DESCRIPTION)
                macro.body = macro_d.get(const.CONF_BODY, {})
                if macro.params_def is not None:
                    macro.params_validator = ParameterValidators.create_schema_for_param_def(macro.params_def)
                meta.macros_def[name] = macro

    @classmethod
    def parse_package_meta(cls, meta_dict: dict, package: PackageDefinition) -> PackageMeta:
        meta = PackageMeta()
        meta_dict = crv.validate_and_normalize(meta_dict, cls.META_SCHEMA).normalized_data
        cls.parse_common(meta, meta_dict, package)
        meta.params_def = meta_dict.get(const.CONF_PARAMS, {})
        meta.export = meta_dict.get(const.CONF_EXPORT, [])
        # Verify if export contains valid variable names
        for i, x in enumerate(meta.export):
            export_name = x[const.CONF_NAME]
            if export_name not in meta.variables.keys():
                raise crv.Invalid(
                    "Export must point existing variables. " 'Variable "{}" is not declared'.format(export_name),
                    [const.CONF_EXPORT, i],
                )
        # Create params validator
        if meta.params_def is not None:
            meta.params_validator = ParameterValidators.create_schema_for_param_def(meta.params_def)
        cls._process_macros(meta, meta_dict, package)
        return meta

    @classmethod
    def parse_root_meta(cls, meta_dict: dict, package: PackageDefinition) -> RootMeta:
        meta = RootMeta()
        meta_dict = crv.validate_and_normalize(meta_dict, cls.META_SCHEMA).normalized_data
        cls.parse_common(meta, meta_dict, package)
        cls._process_macros(meta, meta_dict, package)
        return meta


class PackageProcessor(object):
    DEFAULT_ROOT_FILES = ("main.yaml", "main.yml", "default.yaml", "default.yml")

    def __init__(self, package_loader: Optional[LoaderRegistry] = None) -> None:
        self.package_loader = package_loader if package_loader is not None else DefaultLoaderRegistry.clone()
        self.package_meta_reader = PackageMetaReader()
        self._resource_dir = os.path.join(os.path.dirname(__file__), "resources")
        self.global_packages = ["jbstd"]
        self.secrets: Dict[str, Any] = {}
        self.root_expression_evaluator = RootExpressionEvaluator(None, self.secrets)

    @classmethod
    def resolve_default_file(cls, meta: LoadedDataMeta) -> Optional[str]:
        for x in cls.DEFAULT_ROOT_FILES:
            file_path = os.path.join(meta.path, meta.target_path, x)
            if os.path.isfile(os.path.join(meta.path, meta.target_path, x)):
                return file_path
        return None

    def _load_package_source(self, package_source: PackageSource, package_def: PackageDefinition):
        if isinstance(package_source, dict):
            package_def.content = copy.deepcopy(package_source)
            _LOGGER.warning(
                'You are using outdated syntax for package "%s" definition. '
                "Consider specifying package with string locator e.g. "
                '"local:path/to/package.yaml" (path is relative to the current '
                "yaml file)",
                package_def.local_name,
            )
            return

        if not isinstance(package_source, str):
            raise crv.Invalid(
                "Package source is incorrect. Expected source definition is either"
                "a string locator or dictionary containing package configuration. "
            )
        loaded_meta = self.package_loader.load(package_source)
        package_def.locator = loaded_meta.locator
        package_file = (
            os.path.join(loaded_meta.path, loaded_meta.target_path)
            if loaded_meta.is_file
            else self.resolve_default_file(loaded_meta)
        )
        if not os.path.isfile(package_file):
            raise crv.Invalid(
                "Package path must point either file or folder containing one of " + str(self.DEFAULT_ROOT_FILES),
                ["source"],
            )
        # Read yaml file
        package_dict = load_yaml_config_file(package_file)
        package_def.file_system_location = package_file
        # Recursively load subpackages
        package_def.content = package_dict

    def _load_package(
        self,
        package_name,
        package_config: PackageConfig,
        params_expression_evaluator: ExpressionEvaluator,
        parent: Optional[PackageDefinition] = None,
    ) -> PackageDefinition:
        _validate_package_config(package_name, package_config)
        package = PackageDefinition(package_name, parent)
        if _is_short_package_config_syntax(package_config):
            self._load_package_source(package_config, package)
        else:
            self._load_package_source(package_config[const.CONF_SOURCE], package)
            package_content = none_throws(package.content)
            if const.CONF_PACKAGE in package_content:
                package_meta = self.package_meta_reader.parse_package_meta(
                    package_content.get(const.CONF_PACKAGE, {}), package
                )
                package.meta = package_meta
                # Validate params
                with crv.prepend_path(const.CONF_PARAMS):
                    params = package_config.get(const.CONF_PARAMS, {})
                    params_expression_evaluator.expression_evaluation_pass(params)
                    package.params = package_meta.params_validator(params)
                # Set macros
                package.macros = package.meta.macros_def
                del package_content[const.CONF_PACKAGE]
            if isinstance(package_config[const.CONF_SOURCE], str):
                package.external_ref = package_config[const.CONF_SOURCE]
        return package

    def _handle_outputs(self, package: PackageDefinition, expression_evaluator: ExpressionEvaluator):
        for export in package.meta.export:
            package.outputs[export[const.CONF_NAME]] = package.meta.variables[export[const.CONF_NAME]]

    def do_root_document_pass(self, config: dict, root: PackageDefinition):
        # step 1. Evaluate variables
        _LOGGER.debug("Evaluating variables for root document")
        self.root_expression_evaluator.expression_evaluation_pass(root.meta.variables)
        # step 2. Evaluate the rest of expressions
        _LOGGER.debug("Evaluating expressions for root document")
        self.root_expression_evaluator.expression_evaluation_pass(config)

    def import_standard_packages(self, root: PackageDefinition):
        config = dict(
            packages={
                x: {const.CONF_SOURCE: "local:" + os.path.join(self._resource_dir, x)} for x in self.global_packages
            }
        )
        virtual_root = PackageDefinition.create_virtual_root(config, root.file_system_location)
        with crv.prepend_path("GLOBAL LIB"):
            self.do_packages_pass(config, virtual_root)
        for (
            name,
            pkg,
        ) in virtual_root.packages.items():
            register_global(name, pkg)

    def do_packages_pass(self, config: dict, parent: PackageDefinition):  # noqa: C901
        """
        Packages syntax:
        Short (the old one):
            packages:
                pkg_name: !include folder/file_name.yaml
        Full (the new one):
            packages:
                pkg_name:
                    source: local:folder/file_name.yaml
                    params:
                        var1: 1234
                        var2: abc
        :param config:
        :param parent:
        :return:
        """
        _log_prefix = "\t" * parent.get_depth()
        parent_local_name = (
            "document root" if parent.is_root else "{}({})".format(parent.instance_name, str(parent.locator))
        )
        if parent.is_virtual_root:
            parent_local_name = "standard library"
        if not parent.is_virtual_root:
            _LOGGER.info(_log_prefix + "Processing " + parent_local_name)
            _LOGGER.debug(_log_prefix + "Discovering packages for " + parent_local_name)
        if parent.is_root:
            if not parent.is_virtual_root:
                _LOGGER.info(_log_prefix + "Parsing root document meta")
            parent.meta = self.package_meta_reader.parse_root_meta(  # type: ignore
                config.get(const.CONF_META, {}), parent
            )
            if const.CONF_META in config:
                del config[const.CONF_META]
            # Bootstrapping standard library
            if not parent.is_virtual_root:
                _LOGGER.info("Bootstrapping standard library")
                self.import_standard_packages(parent)
                _LOGGER.info("Standard library initialized. Starting document processing")
                self.root_expression_evaluator = RootExpressionEvaluator(parent, self.secrets)
        if const.CONF_PACKAGES not in config:
            _LOGGER.debug(_log_prefix + "\tNo packages found")
            return config
        packages = config[const.CONF_PACKAGES]
        with crv.prepend_path(const.CONF_PACKAGES):
            if not isinstance(packages, dict):
                raise crv.Invalid("Packages must be a key to value mapping, got {} instead" "".format(type(packages)))

            for package_name, package_config in packages.items():
                with crv.prepend_path(package_name):
                    _LOGGER.debug(_log_prefix + "Found declared package " + package_name)
                    package_name = valid_id(package_name)
                    params_expression_evaluator = (
                        self.root_expression_evaluator if parent.is_root else PackageExpressionEvaluator(parent)
                    )
                    package = self._load_package(package_name, package_config, params_expression_evaluator, parent)
                    _LOGGER.debug(_log_prefix + "\tValidation passed for package " + package_name)
                    expression_evaluator = PackageExpressionEvaluator(package)
                    # Processing cycle
                    # step 1. Evaluate variables
                    _LOGGER.debug(_log_prefix + "Evaluating variables for package " + package_name)
                    expression_evaluator.expression_evaluation_pass(package.meta.variables)
                    # step 2. Process sub-packages
                    _LOGGER.debug(_log_prefix + "Discovering subpackages for " + package_name)
                    recursive_package_content = none_throws(package.content)
                    if isinstance(package_config, dict):
                        recursive_package_content = self.do_packages_pass(recursive_package_content, package)
                    expression_evaluator.refresh_context()
                    # step 3. Evaluate the rest of expressions
                    _LOGGER.debug(_log_prefix + "Evaluating expressions for package " + package_name)
                    expression_evaluator.expression_evaluation_pass(recursive_package_content)
                    # step 4. Evaluate outputs
                    _LOGGER.debug(_log_prefix + "Evaluating outputs for package " + package_name)
                    self._handle_outputs(package, expression_evaluator)
                    parent.packages[package.instance_name] = package
                    if not parent.is_root:
                        config = _merge_package(recursive_package_content, config)
            del config[const.CONF_PACKAGES]
        if parent.is_root:
            self.do_root_document_pass(config, parent)
            for name, pkg in parent.packages.items():
                config = _merge_package(pkg.content, config)
        return config
