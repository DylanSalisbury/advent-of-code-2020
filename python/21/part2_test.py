import unittest
import part2

class Part2Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual('mxmxvkd,sqjhc,fvjkl', part2.solve('test_input.txt'))
    self.assertEqual('fntg,gtqfrp,xlvrggj,rlsr,xpbxbv,jtjtrd,fvjkp,zhszc', part2.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()


