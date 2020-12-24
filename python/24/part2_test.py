import unittest
import part2

class Part2Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(2208, part2.solve('test_input.txt'))
    self.assertEqual(3887, part2.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()


