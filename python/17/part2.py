import util

def solve(input_path):
  f = open(input_path)
  a = util.parse(f, 4)
  for _ in range(6):
    a = util.life_cycle(a)
  return len(a)

if __name__ == '__main__':
    print(solve('input.txt'))