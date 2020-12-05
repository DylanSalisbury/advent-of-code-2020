"""
Count how many of the multi-line input records have all of the required fields
"""

REQUIRED_FIELDS={'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # 'cid' is optional

def complete(record_text):
  fields = record_text.split(' ')
  field_pairs = [x.split(':') for x in fields]
  field_names = {item[0] for item in field_pairs}
  return field_names.intersection(REQUIRED_FIELDS) == REQUIRED_FIELDS

INPUT_PATH="input.txt"

f = open(INPUT_PATH)

result = 0
while (True):
  record_lines = []
  l = ''
  while (True):
    l = f.readline()
    if not l or not l.rstrip():
      break
    record_lines.append(l)
  record_text = ' '.join(record_lines)

  if complete(record_text):
    result = result + 1

  if not l:
    break

print(result)