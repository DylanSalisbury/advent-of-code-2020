import util

def solve(input_path):
  f = open(input_path)
  return len(util.flipped_set(f))

if __name__ == '__main__':
    print(solve('input.txt'))
