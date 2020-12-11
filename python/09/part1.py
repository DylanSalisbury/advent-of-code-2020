import queue
import util

WINDOW_SIZE=25

def solve(input_path):
  f = open(input_path)
  window_queue = queue.Queue()
  window_set = set()
  for _ in range(WINDOW_SIZE):
    n = next(util.next_int(f))
    window_queue.put(n)
    window_set.add(n)

  while (True):
    n = next(util.next_int(f))
    found = False
    for e in window_set:
      if n - e in window_set:
        found = True
        break
    if not found:
      return n
    o = window_queue.get()
    window_set.remove(o)
    window_queue.put(n)
    window_set.add(n)

if __name__ == '__main__':
    print(solve('input.txt'))