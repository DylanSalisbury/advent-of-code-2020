import util

def solve(input_path):
  f = open(input_path)
  future = list(f.readlines())
  current = ''
  iters = 1
  while (current != future):
    current = future
    future = list(util.reseat(iter(current)))
    iters += 1
  print('Total iters: ' + str(iters))
  occupants = 0
  for l in current:
    occupants += l.count('#')
  return occupants

if __name__ == '__main__':
    print(solve('input.txt'))