import util

def solve(input_path):
  f = open(input_path)
  (_, field_spec) = util.read_header(f)
  result = 0
  for l in f:
    ticket = [int(v) for v in l.rstrip().split(',')]
    result += sum(util.ticket_invalid_values(ticket, field_spec))
  return result

if __name__ == '__main__':
    print(solve('input.txt'))