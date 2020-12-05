def seat_spec_to_id(seat_spec):
  row = 0
  for pos in range(7):
    if seat_spec[pos] == 'B':
      row = row + pow(2,6-pos)
      # print("adding row", pow(2,6-pos))
  # print("row", row)
  col = 0
  for pos in range(3):
    if seat_spec[7+pos] == 'R':
      col = col + pow(2,2-pos)
      # print("adding col", pow(2,2-pos))
  # print("col", col)
  return row * 8 + col


