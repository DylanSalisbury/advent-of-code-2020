import util

def solve(input_path):
  f = open(input_path)
  key1 = int(f.readline().rstrip())
  key2 = int(f.readline().rstrip())
  return util.find_encryption_key(7, key1, key2)

if __name__ == '__main__':
    print(solve('input.txt'))