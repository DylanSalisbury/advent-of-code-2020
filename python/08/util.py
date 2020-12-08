"""Helper functions."""
import re

def read_input(input_path):
  f = open(input_path)
  for l in f.readlines():
    yield parse_line(l)

def parse_line(line):
    g = re.match(r'^([a-z]{3}) ([+-]\d+)', line).groups()
    return (g[0], int(g[1]))
