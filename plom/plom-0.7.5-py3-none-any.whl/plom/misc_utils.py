# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2019 Omer Angel
# Copyright (C) 2019, 2021 Colin B. Macdonald
# Copyright (C) 2020 Andrew Rechnitzer
# Copyright (C) 2021 Peter Lee

"""Misc utilities"""

from contextlib import contextmanager
import math
import os
import string
import sys


def format_int_list_with_runs(L, use_unicode=None):
    """Replace runs in a list with a range notation"""
    if use_unicode is None:
        if "UTF-8" in sys.stdout.encoding:
            use_unicode = True
        else:
            use_unicode = False
    if use_unicode:
        rangy = "{}–{}"
    else:
        rangy = "{}-{}"
    L = _find_runs(L)
    L = _flatten_2len_runs(L)
    L = [rangy.format(l[0], l[-1]) if isinstance(l, list) else str(l) for l in L]
    return ", ".join(L)


def _find_runs(S):
    S = [int(x) for x in S]
    S.sort()
    L = []
    prev = -math.inf
    for x in S:
        if x - prev == 1:
            run.append(x)  # noqa
        else:
            run = [x]
            L.append(run)
        prev = x
    return L


def _flatten_2len_runs(L):
    L2 = []
    for l in L:
        if len(l) < 3:
            L2.extend(l)
        else:
            L2.append(l)
    return L2


def next_in_longest_subsequence(items):
    """Guess next entry in the longest unordered contiguous subsequence.

    args:
        items (list): an unordered list of strings.

    return:
        str/None: the next item in a longest subsequence.

    Examples:

    >>> next_in_longest_subsequence(["(a)", "(b)"])
    '(c)'

    >>> next_in_longest_subsequence(["i.", "ii.", "iii."])
    'iv.'

    >>> next_in_longest_subsequence(["2", "1", "C", "(a)", "A", "B"])
    'D'


    >>> next_in_longest_subsequence(["2", "b", "c", "Z", "foo"])

    >>> next_in_longest_subsequence(["a.", "b)", "(c)"])
    'b.'

    Notes:
      * Behaviour in a tie not well-defined; you'll get one of them.
      * "(a), (b)" and "a., b." are different subsequences.
      * The sequences should not be longer than the alphabet.  Overly
        long sequences don't count, e.g., if you already have a-z, then
        that subsequence cannot be extended:

    >>> from string import ascii_lowercase
    >>> next_in_longest_subsequence(["Q1", "Q2", *ascii_lowercase])
    'Q3'
    """
    romans = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]
    romans.extend(["x" + n for n in romans] + ["xx" + n for n in romans])
    smallints = range(1, 31)

    # Each sequence we search is an iterable who iterates are strings
    # (caution: ascii_lowercase is a string not a list).
    sequences = [
        string.ascii_lowercase,
        [f"{x}." for x in string.ascii_lowercase],
        [f"{x})" for x in string.ascii_lowercase],
        [f"({x})" for x in string.ascii_lowercase],
        string.ascii_uppercase,
        [f"{x}." for x in string.ascii_uppercase],
        [f"{x})" for x in string.ascii_uppercase],
        [f"({x})" for x in string.ascii_uppercase],
        romans,
        [f"{x}." for x in romans],
        [f"{x})" for x in romans],
        [f"({x})" for x in romans],
        [f"Q{x}" for x in smallints],
        [f"{x}." for x in smallints],
        [f"{x}" for x in smallints],
    ]

    counts = [0] * len(sequences)
    for idx, seq in enumerate(sequences):
        for count, x in enumerate(seq):
            if x not in items:
                counts[idx] = count
                break

    idx, n = max(enumerate(counts), key=lambda t: t[1])

    if n > 0:
        return sequences[idx][n]

    return None


@contextmanager
def working_directory(path):
    """Temporarily change the current working directory.

    Usage:
    ```
    with working_directory(path):
        do_things()   # working in the given path
    do_other_things() # back to original path
    ```
    """
    current_directory = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_directory)
