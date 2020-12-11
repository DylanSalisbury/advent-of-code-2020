import util
import part1
import queue

def solve(input_path):
  target = part1.solve(input_path)
  f1 = open(input_path)
  l = 0
  r = 0
  min = 0
  max = None
  q = queue.Queue()
  sum = 0
  while (sum < target):
    r = next(util.next_int(f1))
    sum += r
    q.put(r)
    while (sum > target):
      l = q.get()
      sum -= l
    if sum == target:
      min = q.get()
      max = min
      while (not q.empty()):
        e = q.get()
        if e > max:
          max = e
        if e < min:
          min = e
  print (min, max)
  return min + max

if __name__ == '__main__':
    print(solve('input.txt'))