import unittest
import part1

class Part1Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(165, part1.solve('test_input_part1.txt'))
    self.assertEqual(5055782549997, part1.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()


