import util

def solve(input_path):
  f = open(input_path)
  sorted_numbers = sorted(int(s) for s in f)
  prev = 0  # The initial adapter is rated 0
  diff_histogram = [0] * 4
  for n in sorted_numbers:
    diff_histogram[n - prev] += 1
    prev = n
  diff_histogram[3] += 1  # Special case of the device itself
  print(diff_histogram)
  return (diff_histogram[1] * diff_histogram[3])

if __name__ == '__main__':
    print(solve('input.txt'))