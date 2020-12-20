import unittest
import part2

class Part2Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(12, part2.solve('test_input_part2.txt'))
    self.assertEqual(0, part2.solve('input_part2.txt'))

if __name__ == '__main__':
    unittest.main()


