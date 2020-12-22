"""Helper functions."""

import itertools
import re

# s must be a perfectly formatted equation string with no parentheses.
def eval_no_parens(s):
  tokens = s.split(' ')
  result = int(tokens[0])
  for i in range(1,len(tokens),2):
    if tokens[i] == '+':
      result += int(tokens[i+1])
    elif tokens[i] == '*':
      result *= int(tokens[i+1])
    else:
      assert False, 'unexpected operator ' + tokens[i]
  return result

def eval_helper(s, no_paren_helper):
  expression = s
  print('first expression', expression)
  while (True):
    # This matches the first string inside *unnested parentheses*
    m = re.search(r'\(([^\(\)]*)\)', expression)
    if not m:
      return no_paren_helper(expression)
    expression = (
      expression[0:m.start(1)-1]  # -1 to skip opening paren
      + str(no_paren_helper(m.group(1)))
      + expression[m.end(1)+1:])  # +1 to skip closing paren
    print('next expression', expression)

def eval_no_parens_part2(s):
  tokens = s.split(' ')
  while len(tokens) > 2:
    print('tokens', tokens)
    if '+' in tokens:
      i = tokens.index('+')
      tokens = list(itertools.chain.from_iterable([
        tokens[0:i-1],
        [int(tokens[i-1]) + int(tokens[i+1])],
        tokens[i+2:]]))
    elif '*' in tokens:
      i = tokens.index('*')
      tokens = list(itertools.chain.from_iterable([
        tokens[0:i-1],
        [int(tokens[i-1]) * int(tokens[i+1])],
        tokens[i+2:]]))
  return int(tokens[0])

def eval(s):
  return eval_helper(s, eval_no_parens)

def eval_part2(s):
  return eval_helper(s, eval_no_parens_part2)
