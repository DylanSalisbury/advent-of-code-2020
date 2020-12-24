import util

def solve(input_path):
  f = open(input_path)

  # Set of (x, y) pairs identifying tiles
  flipped = set()
  for l in f:
    l = l.rstrip()
    loc = util.rel_from_str(l)
    if loc in flipped:
      flipped.remove(loc)
    else:
      flipped.add(loc)
  return len(flipped)

if __name__ == '__main__':
    print(solve('input.txt'))
