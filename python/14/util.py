"""Helper functions."""

# Represent an int as a list of 36 characters that are digit 0 or 1
def int_to_bits(convert_me):
  result = [0] * 36
  for i in reversed(range(36)):
    result[i] = convert_me % 2
    convert_me /= 2
  return result

def bits_to_int(convert_me):
   result = 0
   for i in range(36):
     result = result * 2 + convert_me[i]
   return result

def apply_mask(mask, input_int):
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

# Input: A list of pairs, either of the form
# ('mask', <mask string>)
# or (<int mem location>, <int value to set>)
#
# Returns a dictionary mapping address int to value int.
def process(l):
  result = dict()
  mask = ['X'] * 36
  for ins in l:
    if ins[0] == 'mask':
      mask = list(ins[1])
    else:
      result[ins[0]] = apply_mask(mask, ins[1])
  return result

# Return all values in a set. (Because set leads to easier unit testing than ordered types)
def apply_mask_part_2(mask, input_int):
  input_bits = int_to_bits(input_int)
  result_bitmasks = [ [ ] ]  # List of lists
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
    
  # print(result_bitmasks)
  result = [ bits_to_int(b) for b in result_bitmasks ]
  # print result
  return result

def process_part_2(l):
  result = dict()
  mask = ['X'] * 36
  for ins in l:
    if ins[0] == 'mask':
      mask = list(ins[1])
    else:
      addresses = apply_mask_part_2(mask, ins[0])
      for a in addresses:
        result[a] = ins[1]
  return result
