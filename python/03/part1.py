"""
Traverse down-1-right-3, wrapping right->left, until reaching the
bottom row. Return the number of # characters hit.

Simple algorithm is to process one line at a time and store a
current X value, which just wraps around when exceeding the
line width.
"""

INPUT_PATH="input.txt"

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

  x = (x + 3) % w
  l = f.readline()
  if not l:
      break

print (result)



