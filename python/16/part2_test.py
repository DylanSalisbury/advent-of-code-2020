import unittest
import part2

class Part2Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(1716, part2.solve('test_input_part2.txt', ''))
    self.assertEqual(3173135507987, part2.solve('input.txt', 'departure'))

if __name__ == '__main__':
    unittest.main()


