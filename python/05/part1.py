"""
Convert each seat code to a seat number, then return the highest number.

There's a clearly useful level of helper function to define that converts
an input string into the ID number. This is because the problem statement
gave us several examples. So testing those examples at that level will help
to verify the code as well as the programmer's understanding of the
instructions.
"""

import util

INPUT_PATH="input.txt"

f = open(INPUT_PATH)

max_id = 0
for l in f.readlines():
  seat_spec = l.rstrip()
  seat_id = util.seat_spec_to_id(seat_spec)
  if (seat_id > max_id):
    max_id = seat_id

print(max_id)  # 896
