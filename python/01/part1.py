'''
Given unsorted list of numbers at https://adventofcode.com/2020/day/1/input
Find the two numbers that add up to 2020 and return their product

Brute force solution
Read numbers into a list or array
With two loops through the list, try every pair of numbers until a pair is found that sums to 2020
Runtime o(n^2)
Memory o(n)

An alternative could use two streaming file handles to read through the input, reducing memory to o(1)

First try at better-runtime solution
Read numbers into list or array
Sort the list
Iterate through every element in the list, as the "first element"
Maintain a second-element index that persists across iterations of the for loop
Second-element index starts pointing to the last (greatest) element of the list
At every iteration of the main loop, reduce second element (if necessary, then as much as necessary) until sum of the pair is <= 2020
If the sum is 2020, return.

This is runtime o(n log n) where n is the size of the input because
The sort is o(n log n)
The main loop iterates at most n times, and
The maximum total number of modifications to the right-side pointer is n

Memory use is o(n) (I think the sort doesn't use more than o(n) memory...)
'''

INPUT_PATH='input.txt'
TARGET_SUM=2020

input_stream = open(INPUT_PATH)
sorted_numbers = sorted(int(s) for s in input_stream)
l = len(sorted_numbers)

l_index = 0
r_index = len(sorted_numbers) - 1
solution = None
while l_index < l:
    target_right = TARGET_SUM - sorted_numbers[l_index]
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

if solution is not None:
    print(solution)
else:
    print('No solution found')
