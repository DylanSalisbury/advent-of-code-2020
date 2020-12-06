"""Helper functions."""

def line_to_set(line):
  return set(line)  # line is iterable

def group_to_set(group_text, intersection = False):
  result = None
  for l in group_text.split('\n'):
    s = line_to_set(l)
    if result is None:
      result = s
    elif intersection:
      result = result.intersection(s)
    else:
      result = result.union(s)
  return result