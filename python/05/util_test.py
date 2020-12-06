import unittest
import util

class UtilTest(unittest.TestCase):

  def test_seat_spec_to_id(self):
    self.assertEqual(567, util.seat_spec_to_id('BFFFBBFRRR'))  # row 70, col 7
    self.assertEqual(119, util.seat_spec_to_id('FFFBBBFRRR'))  # row 14, col 7
    self.assertEqual(820, util.seat_spec_to_id('BBFFBBFRLL'))  # row 102, col 4

if __name__ == '__main__':
    unittest.main()


