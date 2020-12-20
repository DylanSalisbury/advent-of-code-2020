import unittest
import util

class UtilTest(unittest.TestCase):

  def test_bitmask_to_int(self):
    self.assertEquals(278, util.bitmask_to_int( (0, 1, 0, 0, 0, 1, 0, 1, 1, 0) ))
    self.assertEquals(278, util.bitmask_to_int( reversed( (0, 1, 1, 0, 1, 0, 0, 0, 1, 0) )))

  def test_parse(self):
    tiles = util.parse(open('test_input.txt'))
    self.assertEquals(9, len(tiles.keys()))
    self.assertEquals((1, 0, 1, 1, 1, 1, 0, 0, 0, 1), tiles[1951][1])
    for v in tiles.values():
      self.assertEquals(10, len(v))
      for row in v:
        self.assertEquals(10, len(row))
    edges, flipped_edges = util.edges(tiles)
    self.assertEquals(210, edges[0][2311])
    self.assertEquals(89, edges[1][2311])
    self.assertEquals(924, edges[2][2311])
    self.assertEquals(318, edges[3][2311])
    
    self.assertEquals(231, flipped_edges[0][2311])
    self.assertEquals(616, flipped_edges[1][2311])
    self.assertEquals(300, flipped_edges[2][2311])
    self.assertEquals(498, flipped_edges[3][2311])

if __name__ == '__main__':
    unittest.main()


