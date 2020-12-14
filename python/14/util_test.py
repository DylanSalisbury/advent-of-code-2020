import unittest
import util

SEVENTEEN_AS_BITS = [
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 1, 0, 0, 0, 1]

class UtilTest(unittest.TestCase):

  def test_int_to_bits(self):
    self.assertEqual(util.int_to_bits(17), SEVENTEEN_AS_BITS)
    self.assertEqual(util.bits_to_int(SEVENTEEN_AS_BITS),17)

  def test_process(self):
    # Test input from the instructions
    mem = util.process((
        ('mask', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'),
        (8, 11),
        (7, 101),
        (8, 0)))
    self.assertEqual(mem[7], 101)
    self.assertEqual(mem[8], 64)

    # Also test the 11->73 case fro the instructions, which is
    # overridden with the second assignment to location 8 in the
    # previous test call
    mem = util.process((
        ('mask', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'),
        (8, 11)))
    self.assertEqual(mem[8], 73)
    
  def test_apply_mask_part_2(self):
    self.assertEqual(
      set(util.apply_mask_part_2(list('000000000000000000000000000000X1001X'), 42)),
      set( (26, 27, 58, 59) ))
    self.assertEqual(
      set(util.apply_mask_part_2(list('00000000000000000000000000000000X0XX'), 26)),
      set( (16, 17, 18, 19, 24, 25, 26, 27) ))


if __name__ == '__main__':
    unittest.main()


