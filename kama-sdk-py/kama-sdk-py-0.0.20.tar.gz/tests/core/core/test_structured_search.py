import unittest

from kama_sdk.core.core.structured_search import is_terminal_match, is_query_match


class TestStructuredSearch(unittest.TestCase):

  def test_terminal_match_regex(self):
    self.assertTrue(is_terminal_match("exact", "exact"))
    self.assertTrue(is_terminal_match("exact\\..+", "exact.ing"))

    self.assertFalse(is_terminal_match("exact", "inexact"))
    self.assertFalse(is_terminal_match("exact", "exacting"))

  def test_terminal_match_none_false(self):
    self.assertTrue(is_terminal_match(False, False))
    self.assertTrue(is_terminal_match(None, None))
    self.assertTrue(is_terminal_match([False, None], False))
    self.assertTrue(is_terminal_match([False, None], None))

    self.assertFalse(is_terminal_match(False, None))
    self.assertFalse(is_terminal_match(None, False))
    self.assertFalse(is_terminal_match([False, None], ''))
    self.assertFalse(is_terminal_match([False, None], 'None'))

  def test_with_explicit_expr(self):
    self.assertTrue(is_terminal_match("expr::eq::foo", "foo"))
    self.assertTrue(is_terminal_match("expr::defined", "foo"))
    self.assertFalse(is_terminal_match("expr::defined", None))

  def test_terminal_match_list(self):
    self.assertTrue(is_terminal_match(["either", "or"], "either"))
    self.assertTrue(is_terminal_match(["either", "or"], "or"))
    self.assertTrue(is_terminal_match(["either", "or.*"], "oreo"))

    self.assertFalse(is_terminal_match(["either", "or"], "neither"))

  def test_query_match(self):
    self.assertFalse(is_query_match({
      'k': 'k'
    }, challenge_one))

    self.assertTrue(is_query_match({
      'x': 'x'
    }, challenge_one))

    self.assertTrue(is_query_match({
      'x': 'x',
      'z.z': 'z'
    }, challenge_one))

    self.assertFalse(is_query_match({
      'x': 'x',
      'z.z': '!z'
    }, challenge_one))


challenge_one = {
  'x': 'x',
  'y': None,
  'z': {
    'z': 'z'
  }
}
