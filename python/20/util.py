"""Helper functions."""
import re
import itertools

# Return map of tile ID to 2-d list of 0's and 1's
# This map is [row][column] order but most of the rest of the code is the opposite
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

def edges(m):
  result = []
  flip_result = []
  for i in range(4):
    d = dict()
    flip_d = dict()
    for k, v in m.iteritems():
      d[k] = edge(i, v)
      flip_d[k] = flip_int(d[k]) # was edge(i, tuple(reversed(v)))
      # print('edge result', d[k], k, i)
    result.append(d)
    flip_result.append(flip_d)

  return (result, flip_result)

# Return a pair:
# First item is a list of corner tile IDs
# Second item is a list of lists of the corner's two unique edge values
def find_corners(tiles):
  myedges, flipped_edges = edges(tiles)
  corner_tile_ids = []
  corner_unique_sides = []
  all_edge_values = []
  unique_edge_values = set()
  non_unique_edge_values = set()
  super_edges = myedges + flipped_edges
  for i in range(len(super_edges)):
    for v in super_edges[i].values():
      all_edge_values.append(v)
      if v in non_unique_edge_values:
        pass
      elif v in unique_edge_values:
        unique_edge_values.remove(v)
        non_unique_edge_values.add(v)
      else:
        unique_edge_values.add(v)
    
  # print('all_edge_values', sorted(all_edge_values))
  # print('unique_edge_values', sorted(unique_edge_values))
  for t in tiles.keys():
    unique_sides = []
    for i in range(len(myedges)):
      if myedges[i][t] in unique_edge_values:
        unique_sides.append(myedges[i][t])

    if len(unique_sides) == 2:
      corner_tile_ids.append(t)
      corner_unique_sides.append(tuple(unique_sides))

  return (corner_tile_ids, corner_unique_sides)

# Do a 90 degree turn
def rotate(tile_id, tile_map, edges, flipped_edges):
  if (True):
    print('rotate in', tile_id)
    print_tile(tile_id, tile_map, edges, flipped_edges)

  z = edges[0][tile_id]
  edges[0][tile_id] = edges[3][tile_id]
  edges[3][tile_id] = edges[2][tile_id]
  edges[2][tile_id] = edges[1][tile_id]
  edges[1][tile_id] = z

  z = flipped_edges[0][tile_id]
  flipped_edges[0][tile_id] = flipped_edges[3][tile_id]
  flipped_edges[3][tile_id] = flipped_edges[2][tile_id]
  flipped_edges[2][tile_id] = flipped_edges[1][tile_id]
  flipped_edges[1][tile_id] = z

  old_tile = tile_map[tile_id]
  tile_map[tile_id] = tuple([ tuple([old_tile[r][c] for r in reversed(range(10))]) for c in range(10) ])

  if (True):
    print('rotate out', tile_id)
    print_tile(tile_id, tile_map, edges, flipped_edges)

def flip(tile_id, tile_map, edges, flipped_edges):
  if (True):
    print('flip in', tile_id)
    print_tile(tile_id, tile_map, edges, flipped_edges)

  swap_indices = (
    (0, 0),
    (2, 2),
    (1, 3),
    (3, 1)
  )
  for pair in swap_indices:
    edges[pair[0]][tile_id], flipped_edges[pair[1]][tile_id] = (
      flipped_edges[pair[1]][tile_id], edges[pair[0]][tile_id]
    )
  old_tile = tile_map[tile_id]
  tile_map[tile_id] = tuple([tuple([old_tile[c][r] for r in reversed(range(10))]) for c in range(10) ])
  if (True):
    print('flip out', tile_id)
    print_tile(tile_id, tile_map, edges, flipped_edges)

def flip_int(i):
  forward = i
  result = 0
  for _ in range(10):
    result = result * 2 + (forward % 2)
    forward /= 2
  print('flip_int', i, result)
  return result

def mapc(i):
  return (['.', '#'])[i]

def print_tile(tile_id, tile_map, edges, flipped_edges):
  print('TILE ' + str(tile_id))
  for y in range(10):
    l = ''.join([ mapc(tile_map[tile_id][y][x]) for x in range(10)])
    print(l)
  edges_tuple = tuple([edges[e][tile_id] for e in range(4)])
  flipped_edges_tuple = tuple([flipped_edges[e][tile_id] for e in range(4)])
  print('edges', edges_tuple)
  print('flipped_edges', flipped_edges_tuple)

# [y][x] order
def print_2d(m):
  for y in range(len(m)):
    l = ''.join([ mapc(m[y][x]) for x in range(len(m[0]))])
    print(l)

# [y][x] order
def strip_border(old_tile):
  print('STRIP BEFORE')
  print_2d(old_tile)
  new_tile = [ ]
  for y in range(1, len(old_tile) - 1):
    new_tile.append(old_tile[y][1:-1])
  print('STRIP AFTER')
  print_2d(new_tile)
  return new_tile

def print_image(i):
  for l in i:
    print(l)

# Return list of strings.
def create_image(tiles, grid):
  result = []
  for grid_y in range(len(grid[0])):
    row_of_tiles = [ tiles[grid[grid_x][grid_y]] for grid_x in range(len(grid)) ]
    for y in range(len(row_of_tiles[0])):
      # This is an x index into row_of_tiles, i.e. 0 through 11
      # y is the y index of the text in all of the row-of-tiles tiles
      row_of_rows_as_ints = [row_of_tiles[x][y] for x in range(len(row_of_tiles))]
      row_as_ints = itertools.chain.from_iterable(row_of_rows_as_ints)
      print('row_as_ints', row_as_ints)
      result.append(''.join([mapc(n) for n in row_as_ints]))
  print_image(result)
  return result

# Rotates counter-clockwise instead of clockwise but this
# doesn't change the overall result
def text_rotate(input_text):
  output_text = []
  for c in reversed(range(len(input_text[0]))):
    new_row = ''.join([input_text[r][c] for r in range(len(input_text))])
    output_text.append(new_row)
  print('ROTATED')
  print_image(output_text)
  return output_text

def text_flip(input_text):
  output_text = [s[::-1] for s in input_text]
  print('FLIPPED')
  print_image(output_text)
  return output_text

# Change monster bits to O in image and return True if any were found
def highlight_monsters(image):
  # Instead of regular expressions, should just detect monsters by using the
  # highlight_positions coords that are also used to highlight the pixels.
  # That will more naturally find overlapping monsters too.
  
  # Start by searching for the middle row, since it contains the leftmost character
  middle_part_coords = []  # List of y,x coordinates that match monster-middle-strings
  complete_part_coords = []  # Subset of above, for full monsters
  for r in range(1, len(image)-1):
    for c in range(len(image[r])-19):
      if re.match(r'#....##....##....###', image[r][c:c+20]):
        middle_part_coords.append([r, c])
    # Previous code that did not catch monsters whose middle rows overlap!
    #matches = re.finditer(r'#....##....##....###', image[r])
    #for m in matches:
    # middle_part_coords.append([r, m.start()])
  print('middle_part_coords', middle_part_coords)
  for coord in middle_part_coords:
    top_row = image[coord[0] - 1]
    bottom_row = image[coord[0] + 1]
    top_portion = top_row[coord[1]:coord[1] + 20]
    bottom_portion = bottom_row[coord[1]:coord[1] + 20]
    if (re.match(r'..................#.', top_portion)
      and re.match(r'.#..#..#..#..#..#...', bottom_portion)):
      complete_part_coords.append(coord)
  print('complete_part_coords', complete_part_coords)

  for coord in complete_part_coords:
    highlight_positions = (
      (-1, 18), (0, 0), (0, 5), (0, 6), (0, 11), (0, 12), (0, 17), (0, 18), (0, 19),
      (1, 1), (1, 4), (1, 7), (1, 10), (1, 13), (1, 16))
    for h in highlight_positions:
      # Ugh
      a = [c for c in image[coord[0] + h[0]]]
      a[coord[1] + h[1]] = 'O'
      image[coord[0] + h[0]] = ''.join(a)

  if len(complete_part_coords) > 0:
    print_image(image)
    return True
  
  return False

