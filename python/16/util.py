"""Helper functions."""
import re


# Given a file, read and parse everything up to the nearby ticket lines.
# Returns a pair:
# First item is your ticket as a list of integers.
# Second item is a dictionary mapping field names to pairs of pairs of ints.
def read_header(f):
  your_ticket = [1, 2, 3]
  field_spec = dict()

  while (True):
    l = next(f)
    l = l.rstrip()
    if not l:
      break
    m = re.match(r'([a-zA-Z ]+): (\d+)-(\d+) or (\d+)-(\d+)', l)
    field_spec[m.group(1)] = ( (int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5))) )

  _ = next(f)  # Skip 'your ticket:' line
  your_ticket = [int(s) for s in next(f).split(',')]
  _ = next(f)  # Skip blank line
  _ = next(f)  # Skip 'nearby tickets:' line

  return (your_ticket, field_spec)

def ticket_invalid_values(ticket, field_spec):
  result = [ ]
  for v in ticket:
    v_valid = False
    for f in field_spec.values():
      for p in f:
        if (v >= p[0] and v <= p[1]):
          v_valid = True
    if not v_valid:
      result.append(v)
  return result