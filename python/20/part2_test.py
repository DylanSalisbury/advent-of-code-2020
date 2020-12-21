import unittest
import part2

class Part2Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(273, part2.solve('test_input.txt'))
    self.assertEqual(2323, part2.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()


