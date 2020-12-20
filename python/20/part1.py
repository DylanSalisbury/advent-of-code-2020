import util

def solve(input_path):
  corner_tile_ids = []

  f = open(input_path)
  tiles = util.parse(f)
  edges, flipped_edges = util.edges(tiles)
  all_edge_values = []
  unique_edge_values = set()
  non_unique_edge_values = set()
  super_edges = edges + flipped_edges
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
    
  print('all_edge_values', sorted(all_edge_values))
  print('unique_edge_values', sorted(unique_edge_values))
  for t in tiles.keys():
    num_unique_sides = 0
    for i in range(len(edges)):
      if edges[i][t] in unique_edge_values:
        num_unique_sides += 1

    if num_unique_sides == 2:
      corner_tile_ids.append(t)

  print('corner_tile_ids', corner_tile_ids)
  assert len(corner_tile_ids) == 4, 'Wrong number of corners: ' + str(len(corner_tile_ids))
  result = 1
  for i in corner_tile_ids:
    result *= i
  return result

if __name__ == '__main__':
    print(solve('input.txt'))