"""Helper functions."""

# Return map of tile ID to 2-d list of 0's and 1's
def parse(f):
  result = dict()
  done = False
  while (not done):
    charint = { '#': 1, '.': 0 }
    record_lines = []
    l = ''
    while (True):
      try:
        l = next(f).rstrip()
      except StopIteration:
        done = True
        l = ''
      if not l:
        break
      record_lines.append(l)

    # Handle special case of duplicate blank lines at end of real input file.
    if not record_lines:
      continue

    tile_num = int(record_lines[0][5:-1])
    result[tile_num] = tuple([ tuple([charint[c] for c in s ]) for s in record_lines[1:] ])
    #print(record_lines[1:])
    #print(tile_num, result[tile_num])
  return result

def bitmask_to_int(t):
  result = 0
  for e in t:
    result = result * 2 + e
  return result

def edge(n, v):
  if n == 0:
    return bitmask_to_int(v[0])
  if n == 1:
    return bitmask_to_int( r[-1] for r in v )
  if n == 2:
    return bitmask_to_int( reversed(v[-1]) )
  return bitmask_to_int( reversed( [r[0] for r in v] ) )
  
def flip(v):
  return tuple(reversed(v))

def edges(m):
  result = []
  flip_result = []
  for i in range(4):
    d = dict()
    flip_d = dict()
    for k, v in m.iteritems():
      d[k] = edge(i, v)
      flip_d[k] = edge(i, flip(v))
      # print('edge result', d[k], k, i)
    result.append(d)
    flip_result.append(flip_d)

  return (result, flip_result)