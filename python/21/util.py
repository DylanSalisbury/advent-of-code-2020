"""Helper functions."""

import re

# Return a list of pairs, each of which is
# item 0: list of ingredient strings
# item 1: list of allergen strings
#
# Remember that some allergens may be missing, but every input line
# seems to contain a nonzero number of allergen strings.

def parse(f):
  result = []
  for l in f:
    m = re.match(r'^(.*) \(contains (.*)\)\n$', l)
    ingredient_string = m.group(1)
    allergen_string = m.group(2)
    result.append( (ingredient_string.split(' '), allergen_string.split(', ')) )
  return result