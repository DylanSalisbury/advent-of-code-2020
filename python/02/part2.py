"""
Count input lines meeting a certain format:

a-b c: <string>

Where a and b are decimal numbers (may be multi-digit)
c is a single character

The line is a match if exactly one of string index a and
string index b, are character c.
"""

import re

INPUT_PATH="input.txt"

result = 0
f = open(INPUT_PATH)
for line in f:
    (i1, i2, c, s) = re.match('(\d+)-(\d+) (.): (.+)', line).groups()
    i1 = int(i1)
    i2 = int(i2)
    b1 = s[i1-1] == c
    b2 = s[i2-1] == c
    if b1 ^ b2:
        result = result + 1

print (result)



