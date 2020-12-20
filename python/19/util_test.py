import unittest
import util

class UtilTest(unittest.TestCase):

  def test_read_rules(self):
    literal_map, sequence_map, compose_map = util.read_rules(open('test_input_part1_1.txt'))
    self.assertEqual(1, literal_map['a'])
    self.assertEqual(3, literal_map['b'])
    self.assertTrue(0 in sequence_map[(1, 2)])
    self.assertTrue(2 in sequence_map[(1, 3)])
    self.assertTrue(2 in sequence_map[(3, 1)])
    self.assertEquals(compose_map[0], ((1, 2),))
    self.assertEquals(compose_map[2], ((1, 3), (3, 1)))

    # Also make sure the full input file doesn't create any parse errors
    literal_map, sequence_map, _ = util.read_rules(open('input.txt'))

  # Doesn't scale for the real input
  def test_matches(self):
    literal_map, sequence_map, _ = util.read_rules(open('test_input_part1_2.txt'))
    self.assertTrue(0 in util.matches(literal_map, sequence_map, 'ababbb'))
    self.assertTrue(0 in util.matches(literal_map, sequence_map, 'abbbab'))
    self.assertTrue(0 not in util.matches(literal_map, sequence_map, 'bababa'))
    self.assertTrue(0 not in util.matches(literal_map, sequence_map, 'aaabbb'))
    self.assertTrue(0 not in util.matches(literal_map, sequence_map, 'aaaabbb'))

  def test_does_input_match_rule(self):
    (literal_map, _, composition_map) = util.read_rules(open('test_input_part1_2.txt'))
    self.assertTrue(util.does_input_match_rule(literal_map, composition_map, 0, 'ababbb'))
    self.assertTrue(util.does_input_match_rule(literal_map, composition_map, 0, 'abbbab'))
    self.assertFalse(util.does_input_match_rule(literal_map, composition_map, 0, 'bababa'))
    self.assertFalse(util.does_input_match_rule(literal_map, composition_map, 0, 'aaabbb'))
    self.assertFalse(util.does_input_match_rule(literal_map, composition_map, 0, 'aaaabbb'))

if __name__ == '__main__':
    unittest.main()


