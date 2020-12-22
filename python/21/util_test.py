import unittest
import util

class UtilTest(unittest.TestCase):

  def test_parse(self):
    contents = util.parse(open('test_input.txt'))
    self.assertEquals(4, len(contents))
    self.assertEquals('nhms', contents[0][0][3])
    self.assertEquals('dairy', contents[0][1][0])
    self.assertEquals('fish', contents[0][1][1])
    self.assertEquals('fish', contents[3][1][0])
    contents = util.parse(open('input.txt'))
    self.assertEquals(38, len(contents))
    self.assertEquals('nchjqv', contents[37][0][0])
    self.assertEquals('eggs', contents[37][1][0])
    pass

if __name__ == '__main__':
    unittest.main()


