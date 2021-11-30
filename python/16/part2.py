import util

def solve(input_path, prefix_to_sum):
  f = open(input_path)
  (your_ticket, field_spec) = util.read_header(f)
  all_tickets = [ [int(v) for v in l.rstrip().split(',')] for l in f]
  valid_tickets = [ t for t in all_tickets if not util.ticket_invalid_values(t, field_spec) ]
  field_map = determine_fields(field_spec, valid_tickets, 0)
  departure_indices = [ k for k, v in field_map.items() if v.startswith(prefix_to_sum) ]
  result = 1
  for i in departure_indices:
    result *= your_ticket[i]
  return result

cache = {}
def all_in(ranges, values, cache_index_1, cache_index_2):
  i = cache_index_2 + str(cache_index_1) 
  if i in cache:
    # print('Hit cache', i, cache[i])
    return cache[i]
  r = all_in_helper(ranges, values)
  cache[i] = r
  return r

def all_in_helper(ranges, values):
  for v in values:
    if (v < ranges[0][0] or v > ranges[0][1]) and (v < ranges[1][0] or v > ranges[1][1]):
      return False
  return True

fail_cache = set()

# Return a valid map of field names to 0-based index, or None
# Ignore fields <= starting_index (call this with 0 initially)
def determine_fields(field_spec, valid_tickets, starting_index):
  #if (starting_index == 1):
  #  print('Got to', starting_index, field_spec)
  # print('determine_fields', starting_index)
  # We can map each index to valid names.
  # Recursive function
  # For each possibility for index 0
  #   assign that name to index 0
  #   make a copy of data with index and name removed
  #   call recursively

  # Get the possible fields for column 0, then either return or call recursively
  values = [ t[starting_index] for t in valid_tickets ]
  possible_fields = [ k for (k, v) in field_spec.items() if all_in(v, values, starting_index, k) ]
  cache_index = str([k for k in field_spec])
  if cache_index in fail_cache:
    # print('fail_cache hit', cache_index)
    return None
  if len(valid_tickets[0]) == starting_index + 1:
    if not possible_fields:
      fail_cache.add(cache_index)
      # print('Base case failure')
      return None
    # Success, return the first possible match
    # print('Base case success', starting_index, possible_fields[0])
    return { starting_index: possible_fields[0] }

  for p in possible_fields:
    reduced_field_spec = field_spec.copy()
    del reduced_field_spec[p]
    d = determine_fields(reduced_field_spec, valid_tickets, starting_index + 1)
    if d:
      new_d = d.copy()
      new_d[starting_index] = p
      return new_d

  fail_cache.add(cache_index)
  # print('Failure at depth', starting_index)
  return None

if __name__ == '__main__':
    print(solve('input.txt', 'departure'))
