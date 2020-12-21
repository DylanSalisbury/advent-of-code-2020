from collections import deque
from math import sqrt
import util

def solve(input_path):
  f = open(input_path)
  tiles = util.parse(f)

  grid = construct_grid(tiles)
  
  # Now the values of tiles have been flipped and/or rotated
  # and grid is a 2-dimensional array indexed as [x][y].
  for k, v in tiles.iteritems():
    tiles[k] = util.strip_border(v)
  
  # Next make 8 versions of string lists.
  images = [None] * 8
  images[0] = util.create_image(tiles, grid)
  images[1] = util.text_rotate(images[0])
  images[2] = util.text_rotate(images[1])
  images[3] = util.text_rotate(images[2])
  images[4] = util.text_flip(images[3])
  images[5] = util.text_rotate(images[4])
  images[6] = util.text_rotate(images[5])
  images[7] = util.text_rotate(images[6])

  for i in range(len(images)):
    if util.highlight_monsters(images[i]):
      return sum([sum([1 for c in row if c == '#']) for row in images[i]])

def construct_grid(tiles):
  edges, flipped_edges = util.edges(tiles)
  corners, corner_unique_edges = util.find_corners(tiles)
  print('edges', edges)
  print('flipped_edges', flipped_edges)
  i = 0
  while not (set(corner_unique_edges[0]) == set([edges[3][corners[0]], edges[0][corners[0]]])):
    util.rotate(corners[0], tiles, edges, flipped_edges)
    i += 1

  print('top left corner is tile', corners[0], [edges[3][corners[0]], edges[0][corners[0]]])
  print('Rotated ', corners[0], i, 'times')
  util.print_tile(corners[0], tiles, edges, flipped_edges)

  grid_dim = int(sqrt(len(tiles)))
  assert grid_dim * grid_dim == len(tiles), "Can't find grid dimensions, # tiles = " + str(len(tiles))

  # So now corners[0] is rotated to be top-left. We didn't do any check about whether to flip
  # it or not; we just declared that its side that faces up is correct for now.
  #
  # Next we'll assemble the rest of the tiles into a consistent grid, rotating or flipping each
  # as necessary. This consistent grid may still need to be flipped or rotated in its entirety
  # to find sea monsters.

  # grid will be indexed as [x][y]
  grid = [None] * grid_dim
  for i in range(len(grid)):
    grid[i] = [None] * grid_dim
  # print ('grid', grid)

  tiles_to_place = set([t for t in tiles.keys()])
  tiles_to_place.remove(corners[0])
  grid[0][0] = corners[0]

  # print ('tiles_to_place', len(tiles_to_place), tiles_to_place)

  for c in range(grid_dim):
    # Place the top tile in the column, except for column 0 where it's already placed.
    if c != 0:
      print('top... tiles_to_place', len(tiles_to_place), tiles_to_place)
      glue = util.flip_int(edges[1][grid[c-1][0]])  # 1 == right edge
      print ('right glue', glue)
      print('edges', edges)
      print('flipped_edges', flipped_edges)

      # Find the one and only tile left with that side.
      # First check the ones that are face up.
      found = None
      face_down = False
      for t in tiles_to_place:
        for e in range(4):
          if edges[e][t] == glue:
            assert not found, "uh oh" + str((found, t))
            found = t
            print('found', t, 'face up', c, 0)
          if flipped_edges[e][t] == glue:
            assert not found, 'ooopsie'
            found = t
            face_down = True
            print('found', t, 'face down', c, 0)
      if face_down:
        util.flip(found, tiles, edges, flipped_edges)
      while edges[3][found] != glue:  # 3 == left edge
        util.rotate(found, tiles, edges, flipped_edges)
      grid[c][0] = found
      tiles_to_place.remove(found)

    # Place the rest of the column, top to bottom.
    for r in range(1, grid_dim):
      print('tiles_to_place', len(tiles_to_place), tiles_to_place)
      print('r', r)
      prev_tile = grid[c][r-1]
      print('prev_tile', prev_tile)
      glue = util.flip_int(edges[2][prev_tile])  # 2 == bottom edge
      print ('glue', glue)
      # Find the one and only tile left with that side.
      # First check the ones that are face up.
      found = None
      face_down = False
      for t in tiles_to_place:
        for e in range(4):
          if edges[e][t] == glue:
            assert not found, "uh oh" + str((found, t))
            found = t
            print('found', t, 'face up', c, r)
          if flipped_edges[e][t] == glue:
            assert not found, 'ooopsie'
            found = t
            face_down = True
            print('found', t, 'face down', c, r)
      if face_down:
        util.flip(found, tiles, edges, flipped_edges)
      while edges[0][found] != glue:
        util.rotate(found, tiles, edges, flipped_edges)
      grid[c][r] = found
      tiles_to_place.remove(found)
  return grid

if __name__ == '__main__':
    print(solve('input.txt'))