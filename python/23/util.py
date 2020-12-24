"""Helper functions."""

def moves(start, moves):
  cups = [int(c) for c in start]
  current_index = 0
  print('cups', cups)
  print('current_index', current_index)

  for _ in range(moves):
    pickup_values = [None] * 3
    for i in range(3):
      pickup_index = (current_index + 1 + i) % len(cups)
      pickup_values[i] = cups[pickup_index]
      cups[pickup_index] = None  # So search later won't be confused.
    print('pickup_values', pickup_values)
    print('cups after pickup', cups)

    destination_value = 1 + (-1 + (cups[current_index] - 1)) % len(cups)
    while (destination_value not in cups):
      destination_value = 1 + (-1 + destination_value - 1) % len(cups)
    destination_index = cups.index(destination_value)
    print('destination_index', destination_index)

    # Now leave current in place, shift everything else left
    # by three, starting with that next cup after the gap and ending
    # with (including) the destination cup.
    shift_from = (current_index + 4) % len(cups)
    while shift_from != (destination_index + 1) % len(cups):
      cups[(shift_from - 3) % len(cups)] = cups[shift_from]
      cups[shift_from] = None
      shift_from = (shift_from + 1) % len(cups)

    print('cups after shifting before placing', cups)

    for i in range(0,3):
      cups[(destination_index - 2 + i)] = pickup_values[i]

    current_index = (current_index + 1) % len(cups)

    print('cups after placing', cups)
    print('current_index', current_index)

  index_of_one = cups.index(1)
  result_ints = [ cups[(index_of_one + 1 + i) % len(cups)] for i in range(len(cups) - 1) ]
  return ''.join([str(c) for c in result_ints])