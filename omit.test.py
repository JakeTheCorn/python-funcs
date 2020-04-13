import unittest
from omit import omit

class TestOmit(unittest.TestCase):
  def test_simple(self):
    result = omit({'a': 1, 'b': 2}, ['a'])
    self.assertEqual(result, {'b': 2})
  
  def test_nested(self):
    result = omit({'a': {'1a1': 1, '1a2': 2}, 'b': 2}, ['a.1a2'])
    self.assertEqual(result, {'a': {'1a1': 1}, 'b': 2})

  def test_nested_skipping(self):
    result = omit({'a': {'1a1': 1, '1a2': 2}, 'b': {'1b1': 3, '1b2': 4}}, ['a.1a2', 'b.1b2'])
    self.assertEqual(result, {'a': {'1a1': 1}, 'b': {'1b1': 3}})

  def test_prop_skipping(self):
    result = omit({'a': 1, 'b': 2}, ['b', 'c'])
    self.assertEqual(result, {'a': 1})


unittest.main()
