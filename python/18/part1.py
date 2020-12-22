import util

def solve(input_path):
  result = 0
  f = open(input_path)
  for l in f:
    e = util.eval(l)
    print('Line result', e, l)
    result += e
  return result

if __name__ == '__main__':
    print(solve('input.txt'))