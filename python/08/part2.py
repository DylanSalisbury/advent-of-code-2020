import util

def solve(input_path):
  # Use an array so we can edit-in-place without making copies of the whole instruction set.
  instructions = [ x for x in util.read_input(input_path) ]
  for pos in range(len(instructions)):
    saved_instruction = instructions[pos]
    cmd = saved_instruction[0]
    val = saved_instruction[1]
    r = None
    if cmd == 'nop':
      instructions[pos] = ('jmp', val)
      r = final_acc(instructions)
    elif cmd == 'jmp':
      instructions[pos] = ('nop', val)
      r = final_acc(instructions)
    instructions[pos] = saved_instruction
    if r is not None:
      return r
  raise AssertionError("Tried everything but the program never terminated")

# Return final value of acc or None if infinite loop
def final_acc(instructions):
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

    if pos >= len(instructions):
      return acc
  return None


if __name__ == '__main__':
    print(solve('input.txt'))