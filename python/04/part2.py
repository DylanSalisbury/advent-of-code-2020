"""
Count how many of the multi-line input records have all of the required fields
"""

import re

REQUIRED_FIELDS={'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # 'cid' is optional
VALID_ECL={'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def complete(record_text):
  fields = record_text.split(' ')
  field_pairs = [x.split(':') for x in fields]
  field_names = {item[0] for item in field_pairs}
  if field_names.intersection(REQUIRED_FIELDS) != REQUIRED_FIELDS:
    print("Fields missing")
    return False

  field_dict = dict(field_pairs)

  byr = int(field_dict['byr'])
  if byr < 1920 or byr > 2002:
    print("byr check failed")
    return False

  iyr = int(field_dict['iyr'])
  if iyr < 2010 or iyr > 2020:
    print("iyr check failed")
    return False

  eyr = int(field_dict['eyr'])
  if eyr < 2020 or eyr > 2030:
    print("eyr check failed")
    return False

  match = re.match('^(\d+)(cm|in)$', field_dict['hgt'])
  if not match:
    print("hgt check 1 failed")
    return False
  (hgt_num, hgt_unit) = match.groups()
  hgt_num = int(hgt_num)
  if hgt_unit == 'in':
    if (hgt_num < 59 or hgt_num > 76):
      print("hgt check 2 failed")
      return False
  else:
    if hgt_num < 150 or hgt_num > 193:
      print("hgt check 3 failed:", hgt_unit, hgt_num)
      return False

  match = re.match('^#[0-9a-f]{6}$', field_dict['hcl'])
  if not match:
    print("hcl check failed")
    return False

  if field_dict['ecl'] not in VALID_ECL:
    print("ecl check failed", field_dict['ecl'])
    return False

  match = re.match('^\d{9}$', field_dict['pid'])
  if not match:
    print("pid check failed")
    return False

  return True

INPUT_PATH="all_valid.txt"

f = open('input.txt')

result = 0
while (True):
  record_lines = []
  l = ''
  while (True):
    l = f.readline()
    if not l or not l.rstrip():
      break
    record_lines.append(l.rstrip())
  record_text = ' '.join(record_lines)

  if complete(record_text):
    result = result + 1

  if not l:
    break

print(result)  # 160