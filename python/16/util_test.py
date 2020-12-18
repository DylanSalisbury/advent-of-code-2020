import unittest
import util

class UtilTest(unittest.TestCase):

  def test_read_header(self):
    contents = (
"""departure location: 49-627 or 650-970
departure station: 26-400 or 413-965

your ticket:
107,109,163

nearby tickets:
910,308,590
""")
    fake_file = iter([l + '\n' for l in contents.split('\n')])
    (your_ticket, fields) = util.read_header(fake_file)
    self.assertEqual(650, fields['departure location'][1][0])
    self.assertEqual(your_ticket[2], 163)
    self.assertEqual('910,308,590\n', next(fake_file))

if __name__ == '__main__':
    unittest.main()


