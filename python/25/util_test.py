import unittest
import util

class UtilTest(unittest.TestCase):

  def test_transform(self):
    self.assertEqual(5764801, util.transform(1, 7, 8))
    self.assertEqual(17807724, util.transform(1, 7, 11))
    pass

  def test_find_transformations(self):
    self.assertEqual(8, util.find_transformations(7, 5764801))
    self.assertEqual(11, util.find_transformations(7, 17807724))

  def test_find_encryption_key(self):
    self.assertEqual(14897079, util.find_encryption_key(7, 5764801, 17807724))

if __name__ == '__main__':
    unittest.main()


