"""Helper functions."""

# From https://stackoverflow.com/questions/10668341/create-3d-array-using-python
# Unfortunately, Python doesn't make it easy to create a multidimensional array.
def multi_dimensional_list(value, *args):
  #args dimensions as many you like. EG: [*args = 4,3,2 => x=4, y=3, z=2]
  #value can only be of immutable type. So, don't pass a list here. Acceptable value = 0, -1, 'X', etc.
  if len(args) > 1:
    return [ multi_dimensional_list(value, *args[1:]) for col in range(args[0])]
  elif len(args) == 1: #base case of recursion
    return [ value for col in range(args[0])]
  else: #edge case when no values of dimensions is specified.
    return None

def reseat(f):
  prev_line = None
  curr_line = None
  next_line = next(f, None)
  while (next_line):
    prev_line = curr_line
    curr_line = next_line
    next_line = next(f, None)
    out_line = list(curr_line)
    for i in range(len(curr_line) - 1):
      neighbors = 0
      if prev_line:
        if i > 0 and prev_line[i-1] == '#':
          neighbors += 1
        if prev_line[i] == '#':
          neighbors += 1
        if prev_line[i+1] == '#':
          neighbors += 1
      if i > 0 and curr_line[i-1] == '#':
        neighbors += 1
      if curr_line[i+1] == '#':
        neighbors += 1
      if next_line:
        if i > 0 and next_line[i-1] == '#':
          neighbors += 1
        if next_line[i] == '#':
          neighbors += 1
        if next_line[i+1] == '#':
          neighbors += 1
      if out_line[i] == '#' and neighbors >= 4:
        out_line[i] = 'L'
      elif out_line[i] == 'L' and neighbors == 0:
        out_line[i] = '#'
    yield(''.join(out_line))

def top_to_bottom(width, height):
  for y in range(height):
    for x in range(width):
      yield (x, y)

def bottom_to_top(width, height):
  for y in reversed(range(height)):
    for x in range(width):
      yield (x, y)

def left_to_right(width, height):
  for x in range(width):
    for y in range(height):
      yield (x, y)

def right_to_left(width, height):
  for x in reversed(range(width)):
    for y in range(height):
      yield (x, y)

def look(prev, input, look_x, look_y, dim_x, dim_y):
  return (look_x >= 0 and look_y >= 0 and look_x < dim_x and look_y < dim_y and
      (input[look_x][look_y] == '#'
      or (input[look_x][look_y] == '.' and prev[look_x][look_y])))

def reseat_part_2(f):
  input = list()
  for l in f:
    input.append(l.rstrip())
  # Store the dimensions of the input grid, to use for intermediate
  # state variables
  dim_y = len(input)
  dim_x = len(input[0])
  # In production code, we would validate the input above this line,
  # then safely assume it's rectangular in the rest of the code.

  # So there are eight directions, numbered clockwise starting from
  # left-up
  occupied = multi_dimensional_list(False, 8, dim_x, dim_y)
  # print(occupied)

  for (x, y) in top_to_bottom(dim_x, dim_y):
    occupied[0][x][y] = look(occupied[0], input, x-1, y-1, dim_x, dim_y)
    occupied[1][x][y] = look(occupied[1], input, x, y-1, dim_x, dim_y)
  for (x, y) in right_to_left(dim_x, dim_y):
    occupied[2][x][y] = look(occupied[2], input, x+1, y-1, dim_x, dim_y)
    occupied[3][x][y] = look(occupied[3], input, x+1, y, dim_x, dim_y)
  for (x, y) in bottom_to_top(dim_x, dim_y):
    occupied[4][x][y] = look(occupied[4], input, x+1, y+1, dim_x, dim_y)
    occupied[5][x][y] = look(occupied[5], input, x, y+1, dim_x, dim_y)
  for (x, y) in left_to_right(dim_x, dim_y):
    occupied[6][x][y] = look(occupied[6], input, x-1, y+1, dim_x, dim_y)
    occupied[7][x][y] = look(occupied[7], input, x-1, y, dim_x, dim_y)

  output = multi_dimensional_list(' ', dim_x, dim_y)
  counts = multi_dimensional_list(' ', dim_x, dim_y)
  for (x, y) in top_to_bottom(dim_x, dim_y):
    num_occupied = sum(1 for d in range(8) if occupied[d][x][y])
    counts[x][y] = str(num_occupied)
    if input[x][y] == 'L' and num_occupied == 0:
      output[x][y] = '#'
    elif input[x][y] == '#' and num_occupied >= 5:
      output[x][y] = 'L'
    else:
      output[x][y] = input[x][y]

  result_lines = (''.join(output[l]) + '\n' for l in range(len(output)))
  counts_lines = (''.join(counts[l]) for l in range(len(counts)))
  # print('\n')
  # print('\n'.join(counts_lines) + '\n')
  return result_lines
