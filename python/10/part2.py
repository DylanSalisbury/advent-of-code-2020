import util

"""
Hacky solution that won't work with all inputs.
TODO: Replace with a solution using memoization or dynamic programming.

There's only gaps of 1 and 3
Where there's a gap of 3, both adapters are absolutely required
Other adapters are optional, but are they totally optional?
They're totally optional unless there's a run of four or more 1's

9 12 13 14 15 16 19

In that example, from the first pass 13 14 15 would be optional
but you couldn't remove them all or you'd have a 4-gap of 12 16

run of 3 optional
combinations = 7 (2^3 - 1)

What if you have one more

9 12 13 14 15 16 17 20

among 13 14 15 16 you could have various combinations but not only-13 or only-16 or none

run of 4 optional
combinations = 13 (2^4 - 3)

13 14 15 16 17

exclude none, 13, 13 17, 17
combinations = 28 (2^5 - 4)

13 14 15 16 17 18

exclude none, 13, 13 14, 13 15, 13 14 15, 13 17, 13 17 18, 13 18, 14, 14 18, 16, 16 17, 16 18, 16 17 18, 17 18, 18

A performant solution *for our given input* may be to make a first pass then explode exponentially
"""
def solve(input_path):
  f = open(input_path)
  sorted_numbers = sorted(int(s) for s in f)
  l = len(sorted_numbers)
  optional = [True] * l

  prev = 0  # The initial adapter is rated 0
  diff_histogram = [0] * 4
  for i in range(len(sorted_numbers)):
    n = sorted_numbers[i]
    diff_histogram[n - prev] += 1
    if n - prev == 3:
      optional[i - 1] = False
      optional[i] = False

    prev = n
  optional[l - 1] = False  # Special case for device adapter

  run = 0
  optional_run_histogram = [0] * 100
  for b in optional:
    if b:
      run += 1
    else:
      optional_run_histogram[run] += 1
      run = 0

  print(optional)
  print(sum(1 for b in optional if b))
  print(optional_run_histogram)
  return (
    (2 ** optional_run_histogram[1])
    * (4 ** optional_run_histogram[2])
    * (7 ** optional_run_histogram[3]))

if __name__ == '__main__':
    print(solve('input.txt'))