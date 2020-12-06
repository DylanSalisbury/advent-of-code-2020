import util

"""
To shoot for a linear-time algorithm, don't sort the tickets.
Instead, create a Boolean array of seen tickets, then pass
through it one time, applying the rules given in the problem
to find the final answer.

The code below uses a shortcut HIGHEST_POSSIBLE_ID to decide
the size of the original array. This can be higher than the
actual max ticket number without affecting the results (based
on the provided puzzle instructions).

An alternative to get rid of this constant would be to
determine the max ticket ID by adding a linear scan of the
input to the start of this solution. For example we could
read through the file another time just to calculate the
max value, or we could read the values into a list then
pass through that list to get the max value. In the latter
case we could avoid reading the file twice by re-using the
list of tickets instead of reading from the file.
"""

HIGHEST_POSSIBLE_ID = 1000

def solve(input_path):
  occupied = [False] * HIGHEST_POSSIBLE_ID

  f = open(input_path)
  for l in f.readlines():
    seat_spec = l.rstrip()
    seat_id = util.seat_spec_to_id(seat_spec)
    occupied[seat_id] = True

  result = -1
  highest_consecutive_occupied = -1
  for i in range(HIGHEST_POSSIBLE_ID):
    if occupied[i]:
      if highest_consecutive_occupied == -1:
        highest_consecutive_occupied = i
    else:
      if highest_consecutive_occupied != -1:
        result = i
        break

  return(result)

if __name__ == '__main__':
    print(solve('input.txt'))