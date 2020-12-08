import util

def solve(input_path):
  instructions = list(util.read_input(input_path))
  executed = [False] * len(instructions)
  pos = 0
  acc = 0
  while not executed[pos]:
    executed[pos] = True
    cmd = instructions[pos][0]
    val = instructions[pos][1]
    if cmd == 'acc':
      acc = acc + val
      pos = pos + 1
    elif cmd == 'jmp':
      pos = pos + val
    elif cmd == 'nop':
      pos = pos + 1
    else:
      raise AssertionError('Unrecognized operation ' + cmd)
  return acc

if __name__ == '__main__':
    print(solve('input.txt'))