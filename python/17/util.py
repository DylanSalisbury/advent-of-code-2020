"""Helper functions."""

from collections import defaultdict

three_d_neighbor_offsets = []
for x in (-1, 0, 1):
  for y in (-1, 0, 1):
    for z in (-1, 0, 1):
      if (x, y, z) != (0, 0, 0):
        three_d_neighbor_offsets.append((x, y, z))
assert len(three_d_neighbor_offsets) == 26, 'Wrong number of 3D neighbor offsets!'
three_d_neighbor_offsets = tuple(three_d_neighbor_offsets)

four_d_neighbor_offsets = []
for x in (-1, 0, 1):
  for y in (-1, 0, 1):
    for z in (-1, 0, 1):
      for t in (-1, 0, 1):
        if (x, y, z, t) != (0, 0, 0, 0):
          four_d_neighbor_offsets.append((x, y, z, t))
assert len(four_d_neighbor_offsets) == 80, 'Wrong number of 4D neighbor offsets!'
four_d_neighbor_offsets = tuple(four_d_neighbor_offsets)

def parse(f, dimensions):
  assert dimensions == 3 or dimensions == 4, "bad # of dimensions"
  result = set()
  y = 0
  for l in f:
    l = l.rstrip()
    x = 0
    for c in l:
      if (c == '#'):
        if dimensions == 3:
          result.add((x, y, 0))
        else:
          result.add((x, y, 0, 0))
      x += 1
    y += 1
  return result
  
def life_cycle(active):
  dimensions = len(next(active.__iter__()))
  assert dimensions == 3 or dimensions == 4, "bad # of dimensions"
  neighbor_offsets = four_d_neighbor_offsets
  if (dimensions == 3):
    neighbor_offsets = three_d_neighbor_offsets

  # Maps coordinates of any spot that has at least one active neighbor
  # to # of active neighbors
  active_neighbor_counts = defaultdict(lambda: 0)
  for cube in active:
    for o in neighbor_offsets:
      if dimensions == 3:
        neighbor = (cube[0] + o[0], cube[1] + o[1], cube[2] + o[2])
      else:
        neighbor = (cube[0] + o[0], cube[1] + o[1], cube[2] + o[2], cube[3] + o[3])
      active_neighbor_counts[neighbor] += 1

  cubes_to_deactivate = set()
  for cube in active:
    if active_neighbor_counts[cube] != 2 and active_neighbor_counts[cube] != 3:
      cubes_to_deactivate.add(cube)

  cubes_to_activate = set()
  for cube in active_neighbor_counts.keys():
    if not cube in active and active_neighbor_counts[cube] == 3:
      cubes_to_activate.add(cube)

  result = set(active)
  for cube in cubes_to_deactivate:
    result.remove(cube)
  for cube in cubes_to_activate:
    result.add(cube)

  return result
