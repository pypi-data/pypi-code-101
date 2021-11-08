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

import os

from .common import PackageDefinition
from .core import PackageProcessor
from strome.pipeline import PipelineElement, StromeRuntime
from .loader import RepositoryLoader
from ... import const


class PackagesProcessingPipeline(PipelineElement):
    NAME = "esphome-packages"
    REQUIRES = [const.CONTEXT_REPO_MAP]
    PROVIDES = [const.CONTEXT_PACKAGES]

    def __init__(self) -> None:
        super().__init__()
        self.package_processor = PackageProcessor()

    def setup(self, flow_runtime: StromeRuntime, params: dict):
        super().setup(flow_runtime, params)
        default_output_dir = os.path.join(flow_runtime.temp_dir, "repos")
        self.package_processor.package_loader.target_dir = default_output_dir
        flow_runtime.register_output(self, const.CONTEXT_PACKAGES, None)

    def run(self, flow_runtime: StromeRuntime):
        self.package_processor.package_loader.register(
            RepositoryLoader(flow_runtime.get_output(const.CONTEXT_REPO_MAP), self.package_processor.package_loader)
        )
        self.package_processor.secrets = flow_runtime.get_output(const.CONTEXT_SECRETS, {})
        root = PackageDefinition.create_root(flow_runtime.config, flow_runtime.config_path)
        flow_runtime.config = self.package_processor.do_packages_pass(flow_runtime.config, root)
        flow_runtime.register_output(self, const.CONTEXT_PACKAGES, root)
