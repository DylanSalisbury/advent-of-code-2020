"""Helper functions."""

def update_and_recall(last_seen_dict, number_to_play, this_round_ordinal):
  result = 0
  if number_to_play in last_seen_dict:
    result = this_round_ordinal - last_seen_dict[number_to_play]
  last_seen_dict[number_to_play] = this_round_ordinal
  return result

def solve(final_ordinal, initial_numbers):
  assert final_ordinal >= len(initial_numbers), ('final_ordinal %d is too small (min %d)' % (final_ordinal, len(initial_numbers)))

  position_last_seen = dict()
  next_ordinal_to_play = 1
  next_number_to_play = None
  while (next_ordinal_to_play <= len(initial_numbers)):  # <= because counting from 1
    next_number_to_play = update_and_recall(position_last_seen, initial_numbers[next_ordinal_to_play - 1], next_ordinal_to_play)
    # We ignore next_number_to_play, except the last time in the loop - we use that value after the loop
    next_ordinal_to_play += 1  # This is the position of the next number to play

  # At the start of each loop interval, next_ordinal_to_play is the position of the
  # number we will generate next. So when this loops ends we will be ready to
  # determine the final number.

  while next_ordinal_to_play < final_ordinal:
    next_number_to_play = update_and_recall(position_last_seen, next_number_to_play, next_ordinal_to_play)
    next_ordinal_to_play += 1

  # OK, here's the next number, which is the solution to the puzzle.
  return next_number_to_play
