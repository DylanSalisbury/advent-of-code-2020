import util

def solve(input_path):
  corner_tile_ids = []

  f = open(input_path)
  tiles = util.parse(f)

  corner_tile_ids, _ = util.find_corners(tiles)

  print('corner_tile_ids', corner_tile_ids)
  assert len(corner_tile_ids) == 4, 'Wrong number of corners: ' + str(len(corner_tile_ids))
  result = 1
  for i in corner_tile_ids:
    result *= i
  return result

if __name__ == '__main__':
    print(solve('input.txt'))