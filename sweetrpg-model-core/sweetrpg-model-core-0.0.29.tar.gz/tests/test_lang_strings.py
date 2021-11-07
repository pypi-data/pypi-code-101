# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""Test cases for LangString
"""

from sweetrpg_model_core.model.lang import LangString
import locale


def test_default():
    this_locale = locale.getlocale()
    ls = LangString()
    assert ls.get_string() is None
    assert ls.get_string(this_locale) is None


def test_bad_locale():
    ls = LangString('test string')
    assert ls.get_string() == 'test string'
    assert ls.get_string('bogus') is None


def test_set_multiple_strings():
    this_locale = locale.getlocale()
    ls = LangString('test string')
    ls.set_string('prueba de cadena', 'es_MX')
    ls.set_string('Teststring', 'de_DE', make_default=True)
    assert ls.get_string() == 'Teststring'
    assert ls.get_string(this_locale) == 'test string'
    assert ls.get_string('es_MX') == 'prueba de cadena'
    assert ls.get_string('de_DE') == 'Teststring'


def test_str():
    ls = LangString('test string')
    s = str(ls)
    assert isinstance(s, str)
    assert s == 'test string'


# def test_repr():
#     this_locale = locale.getlocale()
#     print(this_locale)
#     ls = LangString()
#     repr = f"{ls!r}"
#     assert this_locale[1] in repr
