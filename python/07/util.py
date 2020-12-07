"""Helper functions."""

import re

# It's a directed graph, not a tree.
# Return a pair of dicts.
# The first pair: color -> this bag contains: list of pairs (num, color)
# The second pair: color -> this bag appears in: list of pairs (num, color)
# For part 1, use color part of second pair
def tree_as_dict(input_path):
  contains = dict()
  parent = dict()
  f = open(input_path)
  for l in f.readlines():
    l = l.rstrip()
    line_list = parse_line(l)

    contains[line_list[0]] = line_list[1:]

    for p in line_list[1:]:
      if p[1] not in parent:
        parent[p[1]] = []
      parent[p[1]].append( (p[0], line_list[0]) )
  return (contains, parent)

# Return a list, first element is bag color, remaining are pairs of (num, color)
def parse_line(input_line):
  result = [ ]
  a = input_line.split(' bags contain ')
  result.append(a[0])
  b = a[1].rstrip().split(', ')  # trailing period
  for c in b:
    d = re.match('(\\d+) (.+) bags?', c)
    if d:
      e = d.groups()
      result.append( (int(e[0]), e[1]) )

  return tuple(result)


