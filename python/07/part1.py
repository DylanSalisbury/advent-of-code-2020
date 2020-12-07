"""

"""

import util

def solve(input_path):
  (contains, parent) = util.tree_as_dict(input_path)
  result = set()

  #parent_tuples = parent['shiny gold']
  a = parent['shiny gold']
  next = [ x[1] for x in a]
  while (next):
    n_next = []
    for color in next:
      if not color in result:
        result.add(color)
        if color in parent:
          a = parent[color]
          next_victims = [ x[1] for x in a ]
          # print ('next victims', next_victims)
          n_next.extend(next_victims)
          
    next = n_next
    # print(next)

  # print(result)
  return len(result)

if __name__ == '__main__':
    print(solve('input.txt'))