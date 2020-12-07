"""

"""

import util

def num_bags(color, contains):
  result = 1
  for pairs in contains[color]:
    result = result + pairs[0] * num_bags(pairs[1], contains)
  return result

def solve(input_path):
  (contains, parent) = util.tree_as_dict(input_path)
  return num_bags('shiny gold', contains) - 1  # Because the question doesn't include the outermost bag.


if __name__ == '__main__':
    print(solve('input.txt'))