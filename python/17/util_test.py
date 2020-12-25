import unittest
import util

class UtilTest(unittest.TestCase):

  def test_parse(self):
    active = util.parse(open('test_input.txt'), 3)
    self.assertEquals(5, len(active))
    active = util.parse(open('test_input.txt'), 4)
    self.assertEquals(5, len(active))

  def test_life_cycle_3d(self):
    active = (
      (0, 0, 0),
      (1, 0, 0),
      (2, 0, 0),
      (2, 1, 0),
      (1, 2, 0)
    )
    active = util.life_cycle(active)
    self.assertEqual(11, len(active))
    active = util.life_cycle(active)
    self.assertEqual(21, len(active))
    active = util.life_cycle(active)
    active = util.life_cycle(active)
    active = util.life_cycle(active)
    active = util.life_cycle(active)
    self.assertEqual(112, len(active))

  def test_life_cycle_4d(self):
    active = (
      (0, 0, 0, 0),
      (1, 0, 0, 0),
      (2, 0, 0, 0),
      (2, 1, 0, 0),
      (1, 2, 0, 0)
    )
    active = util.life_cycle(active)
    self.assertEqual(29, len(active))
    active = util.life_cycle(active)
    active = util.life_cycle(active)
    active = util.life_cycle(active)
    active = util.life_cycle(active)
    active = util.life_cycle(active)
    self.assertEqual(848, len(active))

if __name__ == '__main__':
    unittest.main()


