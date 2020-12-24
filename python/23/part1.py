import util

def solve(input_path):
  f = open(input_path)
  return util.moves(f.readline().rstrip(), 100)

if __name__ == '__main__':
    print(solve('input.txt'))