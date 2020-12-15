import util

def solve(input_path):
  instructions = util.parse_file(input_path)
  mem = util.process_part1(instructions)
  result = sum(i[1] for i in mem.items())
  return result

if __name__ == '__main__':
    print(solve('input.txt'))