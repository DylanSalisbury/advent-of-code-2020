import unittest
import part1

class Part1Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(3, part1.solve('test_input_part1_3.txt'))
    self.assertEqual(285, part1.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()


