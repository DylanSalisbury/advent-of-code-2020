"""
Convert each seat code to a seat number, then return the highest number.

There's a clearly useful level of helper function to define that converts
an input string into the ID number. This is because the problem statement
gave us several examples. So testing those examples at that level will help
to verify the code as well as the programmer's understanding of the
instructions.
"""

import util

def solve(input_path):
  f = open(input_path)

  max_id = 0
  for l in f.readlines():
    seat_spec = l.rstrip()
    seat_id = util.seat_spec_to_id(seat_spec)
    if (seat_id > max_id):
      max_id = seat_id

  return max_id

if __name__ == '__main__':
    print(solve('input.txt'))
