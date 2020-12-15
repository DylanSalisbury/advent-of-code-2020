import re
import util

def solve(input_path):
  f = open(input_path)
  instructions = list()
  for l in f:
    m = re.match(r'mask = ([01X]{36})', l)
    if (m):
      instructions.append(('mask', m.group(1)))
      continue

    m = re.match(r'mem\[(\d+)\] = (\d+)', l)
    if (m):
      instructions.append((int(m.group(1)), int(m.group(2))))
      continue

    raise AssertionError('Unexpected input line: ' + l)

  # print(instructions)
  mem = util.process_part1(instructions)
  # print(mem)
  result = sum(i[1] for i in mem.items())
  # print(result)
  return result


if __name__ == '__main__':
    print(solve('input.txt'))