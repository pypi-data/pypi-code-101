"""Tests for mdpo text utilities."""

import math

import pytest

from mdpo.text import (
    min_not_max_chars_in_a_row,
    parse_escaped_pair,
    parse_strint_0_inf,
    removeprefix,
    removesuffix,
)


@pytest.mark.parametrize(
    ('char', 'text', 'expected_result'), (
        ('`', 'hello `` ``` a `` `', 4),
        ('`', 'hello `` ``` a ```` `', 5),
        ('`', 'hello `` ``` a `` `````', 1),
        ('`', 'hello ` `` ``` a `` `````', 4),

        # as default, 1
        ('`', 'hello', 1),

        # does not work for multiple characters (returns default)
        ('``', 'hello `` ``` a `` `````', 1),
    ),
)
def test_min_not_max_chars_in_a_row(char, text, expected_result):
    assert min_not_max_chars_in_a_row(char, text) == expected_result


@pytest.mark.parametrize(
    ('text', 'expected_key', 'expected_value', 'expected_error'),
    (
        ('foo:bar', 'foo', 'bar', None),
        ('foo:Bar:', 'foo', 'Bar:', None),
        ('foo:   bar:', 'foo', 'bar:', None),
        ('foo: \n  bar:', 'foo', 'bar:', None),
        ('foo:Bar\\:', 'foo', 'Bar\\:', None),
        ('\\:foo:bar', ':foo', 'bar', None),
        (r'foo\\:Bar:baz', 'foo:Bar', 'baz', None),
        (r'foo\\:Bar:baz\\', 'foo:Bar', r'baz\\', None),
        # : at the beginning means escaped
        (r':foo\\:Bar:baz\\', ':foo:Bar', r'baz\\', None),
        ('foo', None, None, ValueError),
        (':', None, None, ValueError),
        ('', None, None, ValueError),
    ),
)
def test_parse_escaped_pair(
    text,
    expected_key,
    expected_value,
    expected_error,
):
    if expected_error:
        with pytest.raises(expected_error):
            parse_escaped_pair(text)
    else:
        key, value = parse_escaped_pair(text)
        assert key == expected_key
        assert value == expected_value


@pytest.mark.parametrize(
    ('value', 'expected_value', 'expected_error'),
    (
        ('1', 1, None),
        ('1.1', 1, None),
        (-1, math.inf, None),
        (-1.1, math.inf, None),
        ('-1', math.inf, None),
        ('-1.1', math.inf, None),
        (0, math.inf, None),
        (-0, math.inf, None),
        ('a', None, ValueError),
        ('inf', math.inf, None),
        ('-inf', math.inf, None),
    ),
)
def test_parse_strint_0_inf(value, expected_value, expected_error):
    if expected_error:
        with pytest.raises(expected_error):
            parse_strint_0_inf(value)
    else:
        assert parse_strint_0_inf(value) == expected_value


@pytest.mark.parametrize(
    ('value', 'prefix', 'expected_value'),
    (
        ('foo', 'fo', 'o'),
        ('bar', 'fo', 'bar'),
    ),
)
def test_removeprefix(value, prefix, expected_value):
    assert removeprefix(value, prefix) == expected_value


@pytest.mark.parametrize(
    ('value', 'suffix', 'expected_value'),
    (
        ('foo', 'oo', 'f'),
        ('bar', 'fo', 'bar'),
    ),
)
def test_removesuffix(value, suffix, expected_value):
    assert removesuffix(value, suffix) == expected_value
