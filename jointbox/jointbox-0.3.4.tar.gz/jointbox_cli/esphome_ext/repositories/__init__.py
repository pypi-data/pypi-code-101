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

import datetime
import os
from os import path
from tempfile import gettempdir
from typing import Any, Dict, List

from cli_rack.loader import LoadedDataMeta, InvalidPackageStructure, DefaultLoaderRegistry
from cli_rack.utils import safe_cast

from jointbox_cli import schema, const
from jointbox_cli.validate import valid_locator
from strome.pipeline import StromeRuntime, PipelineElement
from cli_rack_validation import crv

PARAM_TARGET_DIR = "target-dir"
PARAM_REPO_DIRS = "repo-dirs"
CONF_REPOSITORIES = "repositories"

REPOSITORIES_SCHEMA = crv.Schema(
    crv.Any(
        {schema.valid_id: valid_locator},
        crv.ensure_list(
            crv.Any(valid_locator, {crv.Required(const.CONF_NAME): str, crv.Required(const.CONF_URL): valid_locator})
        ),
    )
)


class RepositoriesProcessingPipeline(PipelineElement):
    NAME = "esphome-repos"
    PROVIDES = [const.CONTEXT_REPO_MAP]
    PARAMS_SCHEMA = crv.Schema(
        {crv.Optional(PARAM_TARGET_DIR): str, crv.Optional(PARAM_REPO_DIRS, default=["packages", "src", ""]): [str]},
        required=False,
    )

    def __init__(self) -> None:
        super().__init__()
        self.output_dir = gettempdir()
        self.repo_root_dirs: List[str] = [""]
        self.repositories_loader = DefaultLoaderRegistry.clone()
        local_loader = self.repositories_loader.get_for_locator("local:nothing")
        if local_loader:
            local_loader.reload_interval = datetime.timedelta(seconds=0)  # force reload for local repo

    def setup(self, flow_runtime: StromeRuntime, _params: dict):
        # HANDLE PARAMS
        default_output_dir = path.join(flow_runtime.temp_dir, "repos")
        params: Dict[str, Any] = self._validate_and_normalize_params(_params).normalized_data
        # PARAM: output dir
        self.output_dir = safe_cast(str, params.get(PARAM_TARGET_DIR, default_output_dir))
        self.repo_root_dirs = safe_cast(List[str], params.get(PARAM_REPO_DIRS))
        self._ensure_dir(self.output_dir)
        self.repositories_loader.target_dir = self.output_dir
        flow_runtime.register_output(self, const.CONTEXT_REPO_MAP, {})

    def _repo_dir_resolver(self, meta: LoadedDataMeta) -> str:
        for x in self.repo_root_dirs:
            if os.path.isdir(os.path.join(meta.path, x)):
                return x
        raise InvalidPackageStructure(
            meta, "On of the following folders must be present in repo root: " + str(self.repo_root_dirs)
        )

    def run(self, flow_runtime: StromeRuntime):
        self.logger.debug("Processing repositories")
        with crv.prepend_path(CONF_REPOSITORIES):
            repositories = crv.validate_and_normalize(
                flow_runtime.config.get(CONF_REPOSITORIES, []), REPOSITORIES_SCHEMA
            ).normalized_data
            # Standardize representation (convert to dict form)
            if isinstance(repositories, list):
                mapped = {}
                for x in repositories:
                    if isinstance(x, str):
                        mapped[x] = x
                    else:
                        mapped[x[const.CONF_NAME]] = x[const.CONF_URL]
                repositories = mapped
        repo_map = {}
        for name, url in repositories.items():
            repo_map[name] = self.repositories_loader.load(url, self._repo_dir_resolver)
        flow_runtime.register_output(self, const.CONTEXT_REPO_MAP, repo_map)
        self.logger.info("Available repositories: " + ", ".join(repositories.keys()))
        del flow_runtime.config[CONF_REPOSITORIES]
