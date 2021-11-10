# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2021 Mathieu Parent <math.parent@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from html import unescape
from logging import getLogger
from posixpath import join as posixpath_join
from typing import Any, Optional, Tuple, Union
from urllib.parse import quote as urlquote, urljoin, urlparse, urlunparse
from urllib.request import parse_keqv_list

from html5lib import parse as html5lib_parse
from packaging.requirements import InvalidRequirement, Requirement
from packaging.utils import canonicalize_name, parse_sdist_filename, parse_wheel_filename
from packaging.version import Version
from requests import Session, codes
from requests.models import Response

from gitlabracadabra.packages.package_file import PackageFile
from gitlabracadabra.packages.source import Source


logger = getLogger(__name__)


class PyPI(Source):
    """PyPI repository."""

    def __init__(  # noqa: WPS211
        self,
        *,
        log_prefix: str = '',
        index_url: Optional[str] = None,
        requirements: Union[str, list[str]],
    ) -> None:
        """Initialize a PyPI repository object.

        Args:
            log_prefix: Log prefix.
            index_url: index-url (default to https://pypi.org/simple).
            requirements: Python requirements as list or string.
        """
        self._log_prefix = log_prefix
        self._index_url = index_url or 'https://pypi.org/simple'
        if isinstance(requirements, str):
            self._requirements = requirements.splitlines()
        else:
            self._requirements = [req for reqs in requirements for req in reqs.splitlines()]

        self._session = Session()

    def __str__(self) -> str:
        """Return string representation.

        Returns:
            A string.
        """
        return 'PyPI repository'

    @property
    def package_files(self) -> list[PackageFile]:
        """Return list of package files.

        Returns:
            List of package files.
        """
        package_files: list[PackageFile] = []
        for requirement_string in self._requirements:
            package_files.extend(self._package_files_from_requirement_string(requirement_string))
        return package_files

    def _package_files_from_requirement_string(self, requirement_string: str) -> list[PackageFile]:
        try:
            req = Requirement(requirement_string)
        except InvalidRequirement:
            logger.warning(
                '%sInvalid requirement "%s"',
                self._log_prefix,
                requirement_string,
            )
            return []
        return self._package_files_from_requirement(req)

    def _package_files_from_requirement(self, req: Requirement) -> list[PackageFile]:
        index_url = self._get_index_url(req.name)
        index_response = self._session.request('get', index_url)
        if index_response.status_code != codes['ok']:
            logger.warning(
                '%sUnexpected HTTP status for PyPI index %s: received %i %s',
                self._log_prefix,
                index_url,
                index_response.status_code,
                index_response.reason,
            )
            return []
        return self._package_files_from_requirement_and_response(req, index_response)

    def _get_index_url(self, project_name: str) -> str:
        loc = posixpath_join(
            self._index_url,
            urlquote(canonicalize_name(project_name)),
        )
        if not loc.endswith('/'):
            loc = '{0}/'.format(loc)
        return loc

    def _package_files_from_requirement_and_response(  # noqa: WPS210
        self,
        req: Requirement,
        response: Response,
    ) -> list[PackageFile]:
        document = html5lib_parse(
            response.content,
            transport_encoding=response.encoding,
            namespaceHTMLElements=False,
        )

        base_url = self._get_base_url(response, document)

        package_files: dict[Version, list[PackageFile]] = {}
        for anchor in document.findall('.//a'):
            version, package_file = self._package_file_from_requirement_and_anchor(req, anchor, base_url)
            if version and package_file:
                if version not in package_files:
                    package_files[version] = []
                package_files[version].append(package_file)

        try:
            best_match = sorted(package_files, reverse=True)[0]
        except IndexError:
            return []
        return package_files[best_match]

    def _get_base_url(self, response: Response, document: Any) -> str:
        base_url = response.url
        for base in document.findall('.//base'):
            href = base.get('href')
            if href is not None:
                base_url = href
                break
        return base_url

    def _package_file_from_requirement_and_anchor(
        self,
        req: Requirement,
        anchor: Any,
        base_url: str,
    ) -> Tuple[Optional[Version], Optional[PackageFile]]:
        if 'href' not in anchor.keys() or anchor.get('data-yanked'):
            return None, None

        parsed_url = urlparse(urljoin(base_url, anchor.get('href')))

        filename = parsed_url.path.split('/')[-1]
        name, ver = self._parse_filename(filename)

        if name is None or ver is None or ver not in req.specifier:
            return None, None

        metadata = parse_keqv_list(parsed_url.fragment.split('&'))

        if 'data-requires-python' in anchor.keys():
            metadata['requires-python'] = unescape(anchor.get('data-requires-python'))

        return ver, PackageFile(
            urlunparse(parsed_url._replace(fragment='')),  # noqa: WPS437
            'pypi',
            name,
            str(ver),
            filename,
            metadata=metadata,
        )

    def _parse_filename(self, filename: str) -> Tuple[Optional[str], Optional[Version]]:
        if filename.endswith('.whl'):
            name, ver, _, _ = parse_wheel_filename(filename)
            return name, ver
        elif filename.endswith('.egg'):
            # Ignore egg files for now
            return None, None
        elif filename.endswith('.tar.gz') or filename.endswith('.zip'):
            return parse_sdist_filename(filename)
        return None, None
