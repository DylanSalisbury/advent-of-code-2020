"""
Traverse down-1-right-3, wrapping right->left, until reaching the
bottom row. Return the number of # characters hit.

Simple algorithm is to process one line at a time and store a
current X value, which just wraps around when exceeding the
line width.
"""

def count_trees(f, x_jump, y_jump):
  f = open(INPUT_PATH)

  # Assume the input is correctly formatted, which also implies that
  # the map width can be determined from the first input line.
  # l will be reused every time throught the loop below
  l = f.readline()
  w = len(l)-1  # minus 1 to ignore the newline character.

  x = 0
  result = 0
  # Since we already read one line, structure this like a do-while loop.
  while (True):
    if l[x] == '#':
      result = result + 1
    x = (x + x_jump) % w
    for _ in range(y_jump):
      l = f.readline()
      if not l:
          break
    if not l:
      break

  return result

INPUT_PATH="input.txt"

print (
  count_trees(INPUT_PATH, 1, 1)
  * count_trees(INPUT_PATH, 3, 1)
  * count_trees(INPUT_PATH, 5, 1)
  * count_trees(INPUT_PATH, 7, 1)
  * count_trees(INPUT_PATH, 1, 2))

