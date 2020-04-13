import unittest
from from_obj_path import from_obj_path

class TestFromObjVal(unittest.TestCase):
  def test_simple(self):
    arg = {'a': 1}
    result, _err = from_obj_path(arg, 'a')
    expectation = 1
    self.assertEqual(result, expectation)

  def test_not_found(self):
    arg = {'a': 1}
    _result, err = from_obj_path(arg, 'b')
    self.assertRegex(str(err) ,r'does not exist')

  def test_nested(self):
    arg = {'a': {'a1': 1}}
    result, _err = from_obj_path(arg, 'a.a1')
    self.assertEqual(result, 1)
    arg = {'a': {'a1': {'a2': 2}}}
    result, _err = from_obj_path(arg, 'a.a1.a2')
    self.assertEqual(result, 2)
  
  def test_fallback(self):
    arg = {'a': {'a1': 1}}
    fallback = 'FALLBACK'
    result, _err = from_obj_path(arg, 'a.a2', fallback)
    self.assertEqual(result, fallback)

unittest.main()
