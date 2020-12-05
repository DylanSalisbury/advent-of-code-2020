"""
Count input lines meeting a certain format:

a-b c: <string>

Where a and b are decimal numbers (may be multi-digit)
c is a single character
The line is a match if the count of occurrences of c in <string> are
between a and b, inclusive.
"""

import collections
import re

INPUT_PATH="input.txt"

result = 0
f = open(INPUT_PATH)
for line in f:
    (min, max, c, s) = re.match('(\d+)-(\d+) (.): (.+)', line).groups()
    min = int(min)
    max = int(max)
    count = collections.Counter(s)[c]
    if count >= min and count <= max:
        result = result + 1

print (result)



