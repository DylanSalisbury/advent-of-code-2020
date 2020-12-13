# l is a list of pairs, where each pair is defined as
# First element is a duration value (periodicity)
# Second value is the required modulu
#
# We are looking for a number that, for every duration, satisfies:
# answer % duration = target.
#
# This algorithm will find the target that satisfies one condition
# at a time.
#
# The key to the algorithm is that, once we have a solution that
# satisfies some of the durations, we can increment it by
# *the product of all the currently-satisfied durations* as many
# times as we want and it will still satisfy those durations.
#
# If all the durations are prime numbers, this algorithm is
# (I think) guaranteed to terminate with a solution.
def solve_helper(l):
  running_solution = 0
  product_of_satisfied_periods = 1
  for (period, target_modulo) in l:
    while (running_solution % period != target_modulo):
      running_solution += product_of_satisfied_periods
    product_of_satisfied_periods *= period
  return running_solution

def solve(input_path):
  f = open(input_path)
  _ = f.readline()  # The given timestamp is not relevant for part 2
  second_line = f.readline().rstrip()
  entries = second_line.split(',')
  list_of_inputs = [ [int(entries[i]), i] for i in range(len(entries)) if entries[i] != 'x']
  for i in range(len(list_of_inputs)):
    if list_of_inputs[i][1] > 0:
      list_of_inputs[i][1] = list_of_inputs[i][0] - (list_of_inputs[i][1] % list_of_inputs[i][0])
  return solve_helper(list_of_inputs)

if __name__ == '__main__':
    print(solve('input.txt'))