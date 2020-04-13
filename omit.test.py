import unittest
import copy

FALLBACK_FLAG = '____FALLBACK_FLAG'

def omit(obj, paths):
  if not isinstance(obj, dict):
    return obj
  collector = copy.deepcopy(obj)
  for path in paths:
    if '.' not in path:
      if collector.get(path):
        del collector[path]
      continue
    sub_paths = path.split('.')

    if len(sub_paths) < 2:
      continue

    first, rest = sub_paths[0], sub_paths[1:]
    val = collector.get(first, FALLBACK_FLAG)
    if val == FALLBACK_FLAG:
      continue
    collector[first] = omit(val, rest)

  return collector

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
