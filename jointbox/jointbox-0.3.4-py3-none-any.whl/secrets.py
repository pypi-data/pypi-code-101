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
from typing import Optional, Any, Dict, List

from jointbox_cli import const
from strome.pipeline import PipelineElement, StromeRuntime
from strome.utils import get_all_existing_files, yaml_file_to_dict, deepmerge_dict


class SecretsManager(object):
    def __init__(self) -> None:
        super().__init__()
        self.secrets: Dict[str, Any] = {}

    def read_secrets(self, file_path: str):
        try:
            data = yaml_file_to_dict(file_path)
        except Exception as e:
            raise ValueError("Unable to read secrets file {}: {}".format(file_path, str(e)))
        if not isinstance(data, dict):
            raise ValueError(
                "Invalid secrets file {}. Expected yaml format for secrets is key-value mapping".format(file_path)
            )
        self.secrets = deepmerge_dict(self.secrets, data)

    def get_secret(self, name: str, default_val: Optional[Any] = None) -> Optional[Any]:
        return self.secrets.get(name, default_val)


class SecretsPipeline(PipelineElement):
    NAME = "secrets"
    PROVIDES = [const.CONTEXT_SECRETS]

    DEFAULT_SECRET_FILE_NAMES: List[str] = ["secrets.yaml", "secrets.yml", ".secrets.yaml", ".secrets.yml"]

    def __init__(self) -> None:
        super().__init__()
        self.secrets_manager = SecretsManager()

    def setup(self, flow_runtime: StromeRuntime, params: dict):
        super().setup(flow_runtime, params)
        flow_runtime.register_output(self, const.CONTEXT_SECRETS, {})

    def run(self, flow_runtime: StromeRuntime):
        secret_files = [
            os.path.join(os.path.dirname(flow_runtime.config_path), x) for x in self.DEFAULT_SECRET_FILE_NAMES
        ]
        secret_files = get_all_existing_files(secret_files)
        for x in secret_files:
            self.secrets_manager.read_secrets(x)
        flow_runtime.register_output(self, const.CONTEXT_SECRETS, self.secrets_manager.secrets)
