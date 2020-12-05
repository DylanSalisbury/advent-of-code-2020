"""
As problem 01 but find 3 numbers that add to 2020

Brute-ish force:
Move old solution to a function, then add a loop calling it with
necessary parameters.
Runtime: O(n^2 log(n))
Memory: O(n)

Note: Make sure not to try counting the same element both times

"""

def product_of_terms(target_sum, sorted_numbers):
    l = len(sorted_numbers)
    l_index = 0
    r_index = l - 1
    solution = None
    while l_index < l:
        target_right = target_sum - sorted_numbers[l_index]
        # The second condition r_index > l_index is to avoid
        # the false positive of choosing the same element twice, in
        # case it's half of the target value but only appears once in
        # the input.
        while (sorted_numbers[r_index] > target_right and r_index > l_index):
            r_index = r_index - 1
        if sorted_numbers[r_index] == target_right:
            solution = sorted_numbers[l_index] * target_right
            break
        l_index = l_index + 1
    return solution

INPUT_PATH="input.txt"
TARGET_SUM=2020

input_stream = open(INPUT_PATH)
all_sorted_numbers = sorted(int(s) for s in input_stream)
l = len(all_sorted_numbers)
solution = None
for first_index in range(l):
    elem = all_sorted_numbers[first_index]
    dual_product = product_of_terms(
        TARGET_SUM-elem, all_sorted_numbers[first_index+1:])
    if dual_product is not None:
        solution = elem * dual_product
        break

if solution is not None:
    print(solution)
else:
    print('No solution found')
