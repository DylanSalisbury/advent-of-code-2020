import unittest
import part2

class Part2Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(1068781, part2.solve('test_input.txt'))
    self.assertEqual(3417, part2.solve('test_input_2.txt'))
    self.assertEqual(754018, part2.solve('test_input_3.txt'))
    self.assertEqual(779210, part2.solve('test_input_4.txt'))
    self.assertEqual(1261476, part2.solve('test_input_5.txt'))
    self.assertEqual(1202161486, part2.solve('test_input_6.txt'))
    self.assertEqual(600691418730595, part2.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()


