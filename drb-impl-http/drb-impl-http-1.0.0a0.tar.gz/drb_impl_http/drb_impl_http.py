import io
import re
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

import requests
from drb import DrbNode
from drb.abstract_node import AbstractNode
from drb.exceptions import DrbException, DrbNotImplementationException
from drb.factory import DrbFactory
from drb.path import ParsedPath


class Download(io.BytesIO):
    def __init__(self, path: str):
        self.__resp = requests.get(path, stream=True).content
        super().__init__(self.__resp)

    def close(self) -> None:
        super().close()
        self.__resp.close()


class DrbHttpNode(AbstractNode):
    def __init__(self, path):
        self._path = path
        self._headers = None

    def __init_header(self):
        if self._headers is None:
            self._headers = requests.head(self._path).headers

    @property
    def name(self) -> str:
        key = ('Content-Disposition', None)
        if key in self.attributes.keys():
            p = re.compile('filename ?= ?"(.*)"')
            res = p.search(self.get_attribute(key[0]))
            if res is not None:
                return res.group(1)
        parsed_uri = urlparse(self._path)
        return parsed_uri.path.split('/')[-1]

    @property
    def children(self) -> List[DrbNode]:
        return []

    @property
    def has_child(self) -> bool:
        return False

    @property
    def namespace_uri(self) -> Optional[str]:
        return None

    @property
    def parent(self) -> Optional[DrbNode]:
        return None

    @property
    def value(self) -> Optional[Any]:
        return None

    @property
    def path(self) -> ParsedPath:
        return ParsedPath(self._path)

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        self.__init_header()
        return {(k, None): v for k, v in self._headers.items()}

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        self.__init_header()
        key = (name, namespace_uri)
        if namespace_uri is None and key in self.attributes.keys():
            return self.attributes[key]
        raise DrbException(f'Attribute not found name: {name}, '
                           f'namespace: {namespace_uri}')

    def has_impl(self, impl: type) -> bool:
        return impl == io.BytesIO

    def get_impl(self, impl: type) -> Any:
        if self.has_impl(impl):
            return Download(self.path.name)
        raise DrbNotImplementationException(
            f'no {impl} implementation found')

    def close(self) -> None:
        pass


class DrbHttpFactory(DrbFactory):

    @staticmethod
    def _create_from_uri_of_node(node: DrbNode):
        uri = node.path.name
        return DrbHttpNode(uri)

    def _create(self, node: DrbNode) -> DrbNode:
        return self._create_from_uri_of_node(node)
