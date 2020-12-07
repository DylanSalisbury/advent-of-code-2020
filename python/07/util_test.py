import unittest
import util

class UtilTest(unittest.TestCase):

  def test_parse_line(self):
    self.assertEqual(
      ('posh chartreuse', (2, 'faded blue'), (2, 'pale plum'), (2, 'posh coral')),
      util.parse_line('posh chartreuse bags contain 2 faded blue bags, 2 pale plum bags, 2 posh coral bags.'))

    self.assertEqual(
      ('clear purple', (4, 'bright red')),
      util.parse_line('clear purple bags contain 4 bright red bags.'))
    self.assertEqual(
      ('shiny crimson',),
      util.parse_line('shiny crimson bags contain no other bags.'))

if __name__ == '__main__':
    unittest.main()


