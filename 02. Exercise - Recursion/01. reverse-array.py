def reverse_array(idx, array):
    if idx == len(array) // 2:
        return
    swap_idx = len(array) - idx - 1
    array[idx], array[swap_idx] = array[swap_idx], array[idx]
    reverse_array(idx + 1, elements)


elements = input().split()

reverse_array(0, elements)
print(' '.join(elements))

# Description
# Write a program that reverses and prints an array. Use recursion.
#
# Examples:
#
# Input:
# 1 2 3 4 5 6
#
# Expected output:
# 6 5 4 3 2 1
