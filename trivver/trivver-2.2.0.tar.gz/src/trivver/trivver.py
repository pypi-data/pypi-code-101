#
# Copyright (c) 2020, 2021  Peter Pentchev <roam@ringlet.net>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
"""Implement the version comparison function."""

import functools
import os
import re

from typing import List, Optional, Tuple  # noqa: H301


_RE_NUM_ALPHA = re.compile(r"(?P<num> [0-9]* ) (?P<alpha> .*) $", re.X)
_RE_NUM_END = re.compile(r"^(?P<prologue> .*? ) (?P<num> [0-9]* ) $", re.X)
_RE_EPOCH = re.compile(
    r"(?: (?P<epoch> [0-9]+ ) : )? (?P<rest> [^:]+ ) $", re.X
)


class InvalidEpochError(ValueError):
    """The version string does not conform to the [epoch:]rest pattern."""


def _version_split_num_alpha(ver: str) -> Tuple[str, str]:
    """Split a version component into a numeric and an alphanumeric part.

    "2a" is split into ('2', 'a').
    """
    match = _RE_NUM_ALPHA.match(ver)
    assert match is not None
    data = match.groupdict()
    return data["num"], data["alpha"]


def _version_compare_split_empty(
    spl_a: List[str], spl_b: List[str]
) -> Optional[int]:
    """Check if any of the split version numbers is empty."""
    if not spl_a:
        if not spl_b:
            return 0
        if _version_split_num_alpha(spl_b[0])[0] == "":
            return 1
        return -1
    if not spl_b:
        if _version_split_num_alpha(spl_a[0])[0] == "":
            return -1
        return 1

    return None


def _version_compare_split_comp_int(comp_a: str, comp_b: str) -> Optional[int]:
    """Compare a single component of split version numbers."""
    if comp_a != "":
        if comp_b != "":
            num_a, num_b = int(comp_a, 10), int(comp_b, 10)
            if num_a < num_b:
                return -1
            if num_a > num_b:
                return 1
        else:
            return 1
    elif comp_b != "":
        return -1

    return None


def _version_compare_split_comp_str(comp_a: str, comp_b: str) -> Optional[int]:
    """Compare strings, possibly recursing into version_compare_split()."""
    if comp_a == comp_b:
        return None

    def get_prefix() -> Tuple[Optional[int], str, str]:
        """Determine the common prefix, leaving trailing digits out."""
        prefix = os.path.commonprefix([comp_a, comp_b])
        if comp_a.startswith(prefix + "~"):
            return -1, "", ""
        if comp_b.startswith(prefix + "~"):
            return 1, "", ""

        if prefix:
            match_dig = _RE_NUM_END.match(prefix)
            if match_dig:
                prefix = match_dig.group("prologue")

        rest_a, rest_b = comp_a[len(prefix) :], comp_b[len(prefix) :]
        if rest_a == "":
            return -1, "", ""
        if rest_b == "":
            return 1, "", ""

        return None, rest_a, rest_b

    res, comp_a, comp_b = get_prefix()
    if res is not None:
        return res

    # If they both start with numbers, go recurse.
    if comp_a[0] in "0123456789" and comp_b[0] in "0123456789":
        res = version_compare_split([comp_a], [comp_b])
        return None if res == 0 else res

    if comp_a < comp_b:
        return -1
    return 1


def version_compare_split(spl_a: List[str], spl_b: List[str]) -> int:
    """Compare two version numbers already split into component lists.

    Returns -1, 0, or 1 for the first version being less than, equal to,
    or greater than the second one.
    """
    res = _version_compare_split_empty(spl_a, spl_b)
    if res is not None:
        return res

    (first_a, first_b) = (spl_a.pop(0), spl_b.pop(0))
    (num_a, rem_a) = _version_split_num_alpha(first_a)
    assert num_a != "" or rem_a != "", "could not split " + first_a
    (num_b, rem_b) = _version_split_num_alpha(first_b)
    assert num_b != "" or rem_b != "", "could not split " + first_b

    res = _version_compare_split_comp_int(num_a, num_b)
    if res is not None:
        return res

    res = _version_compare_split_comp_str(rem_a, rem_b)
    if res is not None:
        return res

    return version_compare_split(spl_a, spl_b)


def _version_compare_split_dash(spl_a: List[str], spl_b: List[str]) -> int:
    """Compare two lists of dash-separated dot-containing components.

    Returns -1, 0, or 1 for the first version being less than, equal to,
    or greater than the second one.
    """
    res = _version_compare_split_empty(spl_a, spl_b)
    if res is not None:
        return res

    (first_a, first_b) = (spl_a.pop(0), spl_b.pop(0))
    res = version_compare_split(first_a.split("."), first_b.split("."))
    if res != 0:
        return res

    return _version_compare_split_dash(spl_a, spl_b)


def parse_epoch(ver: str) -> Tuple[str, str]:
    """Retrieve an epoch if there is one, otherwise return "0"."""
    data = _RE_EPOCH.match(ver)
    if data is None:
        raise InvalidEpochError(ver)

    return data.group("epoch") or "0", data.group("rest")


def compare(ver_a: str, ver_b: str) -> int:
    """Compare two version numbers as strings.

    Returns -1, 0, or 1 for the first version being less than, equal to,
    or greater than the second one.
    """
    (ep_a, rest_a), (ep_b, rest_b) = parse_epoch(ver_a), parse_epoch(ver_b)
    res = _version_compare_split_comp_int(ep_a, ep_b)
    if res is not None:
        return res

    return _version_compare_split_dash(rest_a.split("-"), rest_b.split("-"))


key_compare = functools.cmp_to_key(compare)  # pylint: disable=invalid-name

__all__ = ("compare", "key_compare")
