import util

def solve(input_path):
  f = open(input_path)
  my_timestamp = int(f.readline())
  second_line = f.readline().rstrip()
  entries = second_line.split(',')
  bus_durations = [int(s) for s in entries if s != 'x']
  print(bus_durations)

  best_bus = None
  best_delay = None
  for d in bus_durations:
    this_delay = my_timestamp % d  # How long since the last departure
    if this_delay > 0:
      this_delay = d - this_delay  # How long until the next departure
    if best_delay is None or this_delay < best_delay:
      best_delay = this_delay
      best_bus = d

  print(best_bus, best_delay)
  return best_bus * best_delay

if __name__ == '__main__':
    print(solve('input.txt'))