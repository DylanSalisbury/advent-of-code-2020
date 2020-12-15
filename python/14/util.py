"""Helper functions."""

# Represent an int as a list of 36 integers that are each either 0 or 1
def int_to_bits(convert_me):
  result = [0] * 36
  for i in reversed(range(36)):
    result[i] = convert_me % 2
    convert_me /= 2
  return result

# Convert a bitmap (as list of 36 integers that are each either 0 or 1) to int
def bits_to_int(convert_me):
   result = 0
   for i in range(36):
     result = result * 2 + convert_me[i]
   return result

# Apply bitmask (as list of 36 characters) to an int,
# returning an int, according to the part1 rules:
# 'X' means the input bit is unchanged.
# '0' or '1' means the input bit is replaced by 0 or 1.
def apply_mask_part1(mask, input_int):
  input_bits = int_to_bits(input_int)
  output_bits = [0] * 36
  for i in range(36):
    if mask[i] == '0':
      output_bits[i] = 0
    elif mask[i] == '1':
      output_bits[i] = 1
    elif mask[i] == 'X':
      output_bits[i] = input_bits[i]
    else:
      raise AssertionError('Unexpected bitmask element ' + mask[i])
  return bits_to_int(output_bits)

# Run the program according to the rules of Part 2.
#
# Input: A list of pairs, either of the form
# ('mask', <mask string>)
# or (<int mem location>, <int value to set>)
#
# Returns a dictionary mapping address int to value int.
def process_part1(l):
  result = dict()
  mask = ['X'] * 36
  for ins in l:
    if ins[0] == 'mask':
      mask = list(ins[1])
    else:
      result[ins[0]] = apply_mask_part1(mask, ins[1])
  return result

# Apply bitmask (as list of 36 characters) to an int
# returning a list of ints, according to the part2 rules:
# '0' means the input bit is unchanged.
# '1' means the input bit is replaced by 1.
# 'X' means the output list must contain each case of this bit being
#  0 or 1 (along with other permutations for other X's in the bitmask)
def apply_mask_part2(mask, input_int):
  input_bits = int_to_bits(input_int)
  # This is a list of lists, initialized to hold one empty list.
  # This will build all the results, each in (list of integers) form.
  # We build this result by either appending the next bit to EACH of
  # the outputs, or (when we see an X), duplicating each list then
  # appending 0 to half and 1 to the other half.
  result_bitmasks = [ [ ] ]
  for i in range(36):
    if mask[i] == '1':
      for l in result_bitmasks:
        l.append(1)
    elif mask[i] == '0':
      for l in result_bitmasks:
        l.append(input_bits[i])
    elif mask[i] == 'X':
      more_bitmasks = [ list(elem) for elem in result_bitmasks ]
      for l in result_bitmasks:
        l.append(0)
      for l in more_bitmasks:
        l.append(1)
      result_bitmasks.extend(more_bitmasks)
    else:
      raise AssertionError('Unknown bitmask element ' + mask[i])

  # Now convert the results to integers.    
  result = [ bits_to_int(b) for b in result_bitmasks ]
  return result

# Run the program according to the rules of Part 2.
#
# Input: A list of pairs, either of the form
# ('mask', <mask string>)
# or (<int mem location>, <int value to set>)
#
# Returns a dictionary mapping address int to value int.
def process_part2(l):
  result = dict()
  mask = ['X'] * 36
  for ins in l:
    if ins[0] == 'mask':
      mask = list(ins[1])
    else:
      addresses = apply_mask_part2(mask, ins[0])
      for a in addresses:
        result[a] = ins[1]
  return result
