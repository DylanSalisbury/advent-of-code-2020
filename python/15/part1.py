import util

def solve(input_path):
  f = open(input_path)
  nums = [ int(s) for s in f.readline().split(',') ]
  return util.solve(2020, nums)

if __name__ == '__main__':
    print(solve('input.txt'))