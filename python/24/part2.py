from collections import defaultdict
import util

OFFSETS = tuple([v for v in util.POSITIONS.values()])

def life(black):
  tiles_to_turn_white = set()
  for tile in black:
    adjacent_black = set([(tile[0]+o[0], tile[1]+o[1]) for o in OFFSETS]).intersection(black)
    if len(adjacent_black) == 0 or len(adjacent_black) > 2:
      tiles_to_turn_white.add(tile)

  count_black_neighboring_tiles = defaultdict(lambda: 0)
  for tile in black:
    for o in OFFSETS:
      pos = (tile[0] + o[0], tile[1] + o[1])
      count_black_neighboring_tiles[pos] += 1
  # Now remove any that were initially black
  for tile in black:
    if tile in count_black_neighboring_tiles:
      del count_black_neighboring_tiles[tile]
  
  # Now extract any with exactly 2 neighboring black tiles
  tiles_to_turn_black = []
  for (k, v) in count_black_neighboring_tiles.items():
    if v == 2:
      tiles_to_turn_black.append(k)

  for tile in tiles_to_turn_white:
    black.remove(tile)
  for tile in tiles_to_turn_black:
    black.add(tile)

def solve(input_path):
  f = open(input_path)
  black = util.flipped_set(f)
  for d in range(100):
    # print('Day ' + str(d) + ' len ' + str(len(black)))
    life(black)
  return len(black)

if __name__ == '__main__':
    print(solve('input.txt'))