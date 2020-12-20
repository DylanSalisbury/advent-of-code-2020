"""Helper functions."""

# There's 135 rules.
# 2 literal rules and 133 composed rules.
# Each literal rule is one unique character.
# So an input corresponds to only one ordered list of literal rule matches.
#

from collections import deque
from collections import defaultdict
import re

# Given a file, read and parse everything up to the list of input strings, if present
# Returns a tuple:
#
# First item is dictionary mapping single character to rule number that matches it.
# Second item is a dictionary mapping tuple of ints to rules that matches (key states in order).
# Third item is a dictionary mapping int to a tuple of tuples. The leaf items are ordered
# rules as ints.
#
# The "or" operator isn't explictly represented - it's just implicit because the second
# dictionary will contain two key entries mapping to some particular value.
def read_rules(f):
  literal_map = dict()
  sequence_map = defaultdict(lambda: set())
  compose_map = dict()

  try:
    while (True):
      l = next(f)
      l = l.rstrip()
      if not l:
        break
      m1 = re.match(r'^(\d+): "(.)"$', l)
      m2 = re.match(r'^(\d+): (.*)$', l)
      assert m1 or m2, 'Unrecognized input in rule section: <' + l + '>'
      if m1:
        literal_map[m1.group(2)] = int(m1.group(1))
      elif m2:
        defined_rule = int(m2.group(1))
        compose_list = []
        for text_sequence in m2.group(2).split(' | '):
          key = tuple([int(s) for s in text_sequence.split(' ')])
          value = defined_rule
          sequence_map[key].add(value)
          compose_list.append(key)
        assert defined_rule not in compose_map, "compose_map collision"
        compose_map[defined_rule] = tuple(compose_list)

    _ = next(f)  # Skip blank line
  except StopIteration:
    pass  # Some rules contain only rules.

  return (literal_map, sequence_map, compose_map)

# Algorithm to see which rules match a given input
# prev_matches holds rules matched from previous input, init [ ]
# For each input character
#   this_rule = (literal matching rule)
#   for each rule containing this_rule
#
# Create map of characters to single-char rules
# Create map of pair-of-rules to matching parent.
# (Don't need to explicitly represent the or symbol)
#
# Valid_rule_sequences = queue of lists: [ [a a b b c] ]
# matching_single_rules = [ ]
#
# while valid_rule_sequence isn't empty
#   pop sequence from valid_rule_sequences
#   # if it's a single element sequence, add to matching_single_rules
#   for i in range(len(sequence)-1):
#       if sequence[i] and sequence[i+1] match a rule
#         push a new valid rule sequence
#   

def matches(literal_map, sequence_map, s):
  result = []
  literal_rule_sequence = [ literal_map[c] for c in s ]
  valid_rule_sequences = deque()
  valid_rule_sequences.append(literal_rule_sequence)
  while (valid_rule_sequences):
    # print('len', len(valid_rule_sequences))
    sequence = valid_rule_sequences.popleft()
    if len(sequence) == 1:
      # print('Found single match', sequence[0])
      result.append(sequence[0])
    for i in range(len(sequence)):
      for j in range(i+1, len(sequence)+1):
        k = tuple(sequence[i:j])
        # print('sequence is', sequence, 'trying', k)
        v = sequence_map[k]
        if v:
          for r in v:
            new_sequence = sequence[0:i] + [r] + sequence[j:len(sequence)]
            # print('Adding new sequence', new_sequence)
            if new_sequence in valid_rule_sequences:
              # print("It's a dup")
              pass
            else:
              valid_rule_sequences.append(new_sequence)

  return result

# Cache will make unit tests fail.
# cache = dict()

def prefix_lengths_matched(literal_map, composition_map, rule, s):
  if len(s) == 0:
    return []
  if rule in literal_map.values():
    if rule == literal_map[s[0]]:
      return [1]
    return []
  
  #if (rule, s) in cache:
  #  return cache[(rule, s)]

  result = set()
  for rule_sequence in composition_map[rule]:
    # print('trying rule_sequence', rule_sequence)
    match_lengths_for_this_sequence = set([0])
    for sub_rule in rule_sequence:
      newmlfts = set()
      for ml in match_lengths_for_this_sequence:
        for z in prefix_lengths_matched(
          literal_map, composition_map, sub_rule, s[ml:]
        ):
          newmlfts.add(ml + z) 
      match_lengths_for_this_sequence = newmlfts
    for z in match_lengths_for_this_sequence:
      result.add(z)
  # print('returning', result, rule, s)
  #cache[(rule, s)] = result
  return result

def does_input_match_rule(literal_map, composition_maps, rule, s):
  ps = prefix_lengths_matched(literal_map, composition_maps, rule, s)
  # print('ps', ps)
  return len(s) in ps
