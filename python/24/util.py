"""Helper functions."""

# A technique that seems appropriate for part 1 is:
#
# Identify the location of each hex grid as some coordinate pair
# with which we can do navigational math.
#
# That will let us move around and reference tiles without worrying
# about how many tiles there are.
#
# For example, east moves (+2, 0), northeast moves (+1, +1).
# THen we can use ints for everything.

POSITIONS = {
  'w': (-2, 0),
  'e': (2, 0),
  'nw': (-1, 1),
  'ne': (1, 1),
  'sw': (-1, -1),
  'se': (1, -1)
}

# input: list of strings like 'ne', 'e', ...
# output: (x, y) offset pair where positive x = east, positive y = north.
def relative_position(move_list):
  result = [0, 0]
  for m in move_list:
    move_offset = POSITIONS[m]
    result[0] += move_offset[0]
    result[1] += move_offset[1]
  return tuple(result)

def generate_moves(s):
  i = 0
  # Loop is structured like this because it may get incremented again
  # inside the loop.
  while (i < len(s)):
    c = s[i]
    if c == 'w' or c == 'e':
      yield c
    else :
      yield (c + s[i+1])
      i += 1
    i += 1

def rel_from_str(s):
  return relative_position(generate_moves(s))

def flipped_set(f):
  flipped = set()
  for l in f:
    l = l.rstrip()
    loc = rel_from_str(l)
    if loc in flipped:
      flipped.remove(loc)
    else:
      flipped.add(loc)
  return flipped
