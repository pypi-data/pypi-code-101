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

import logging
import os
from typing import Dict, Optional, Union, Callable

from cli_rack.loader import BaseLoader, LoadedDataMeta, BaseLocatorDef, LoaderError, LoaderRegistry


class RepositoryLocatorDef(BaseLocatorDef):
    PREFIX = "repo"
    TYPE = "repo"
    PATH_SEPARATOR = "/"

    def __init__(
        self, repo_name: str, path: str, name: Optional[str] = None, original_locator: Optional[str] = None
    ) -> None:
        self.repo_name = repo_name
        self.path = path
        self.name = name if name is not None else self.__generate_name()
        super().__init__(name, original_locator)

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update(dict(repo_name=self.repo_name, path=self.path, name=self.name))
        return result

    @classmethod
    def from_dict(cls, locator_dict: dict):
        return cls(
            locator_dict["repo_name"], locator_dict["path"], locator_dict["name"], locator_dict.get("original_locator")
        )

    def __generate_name(self):
        return "-".join((self.repo_name, self.generate_hash_suffix(self.path)))


class RepositoryLoader(BaseLoader):
    LOCATOR_CLS = RepositoryLocatorDef
    _STATIC_PREFIX = LOCATOR_CLS.PREFIX + BaseLoader.LOCATOR_PREFIX_DELIMITER

    def __init__(
        self, repos: Dict[str, LoadedDataMeta], package_loader: LoaderRegistry, target_dir="tmp/external"
    ) -> None:
        super().__init__(logging.getLogger("loader.repo"), target_dir)
        self.repositories = repos
        self.package_loader = package_loader
        self.reload_interval = None  # Disable cache

    @classmethod
    def locator_to_locator_def(cls, locator_str: Union[str, BaseLocatorDef]) -> RepositoryLocatorDef:
        if isinstance(locator_str, str):
            # Parse locator
            if not locator_str.startswith(cls._STATIC_PREFIX):
                raise ValueError("Locator should start with " + cls._STATIC_PREFIX)
            _locator = locator_str.replace(cls._STATIC_PREFIX, "", 1)
            locator_components = _locator.split(cls.LOCATOR_CLS.PATH_SEPARATOR, 1)
            if len(locator_components) != 2:
                raise ValueError("Repository locator should be in form repo://repo-name/path/to/file-or-dir")
            repo_name, path = locator_components[0], locator_components[1]
            return RepositoryLocatorDef(repo_name, path, original_locator=locator_str)
        elif isinstance(locator_str, RepositoryLocatorDef):
            return locator_str
        else:
            raise ValueError(
                "Locator should be either locator string or RepositoryLocatorDef got {}".format(
                    locator_str.__class__.__name__
                )
            )

    def load(
        self,
        locator_: Union[str, BaseLocatorDef],
        target_path_resolver: Optional[Callable[[LoadedDataMeta], str]] = None,
        force_reload=False,
    ) -> LoadedDataMeta:

        self._logger.info("Loading " + str(locator_))
        locator = self.locator_to_locator_def(locator_)
        if locator.repo_name not in self.repositories:
            raise LoaderError("Unable to load {}. Unknown repository {}".format(str(locator_), locator.repo_name))
        repo_meta = self.repositories[locator.repo_name]

        meta = LoadedDataMeta.from_dict(
            repo_meta.to_dict(), os.path.join(repo_meta.path, repo_meta.target_path), self.package_loader
        )
        meta.target_path = locator.path
        full_path = os.path.join(meta.path, meta.target_path)
        if not os.path.exists(full_path):
            other_files = os.listdir(os.path.dirname(full_path))
            alternatives_str = ("\n\tPossible options: " + ", ".join(other_files)) if len(other_files) > 0 else ""
            raise LoaderError(
                "Invalid path within repository {}. {} doesn't exist.".format(repo_meta.locator, locator.path)
                + alternatives_str
            )
        meta.is_file = os.path.isfile(full_path)
        return meta
