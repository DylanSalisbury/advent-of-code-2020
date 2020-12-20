import util

def solve(input_path):
  f = open(input_path)
  literal_map, _, composition_map = util.read_rules(f)
  result = 0
  for s in f:
    s = s.rstrip()
    if util.does_input_match_rule(literal_map, composition_map, 0, s):
      result += 1
  return result

if __name__ == '__main__':
    print(solve('input_part2.txt'))