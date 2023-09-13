def nested_loops(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    for num in range(1, len(arr) + 1):
        arr[idx] = num
        nested_loops(idx + 1, arr)


n = int(input())
array = [None] * n

nested_loops(0, array)

# Description
# Write a program that simulates the execution of n nested loops from 1 to n which prints the values of all its
# iteration variables at any given time on a single line. Use recursion.
#
# Examples:
#
# Input:
# 2
#
# Expected output:
# 1 1
# 1 2
# 2 1
# 2 2
#
#
# Input:
# 3
#
# Expected output:
# 1 1 1
# 1 1 2
# 1 1 3
# 1 2 1
# 1 2 2
# ...
# 3 2 3
# 3 3 1
# 3 3 2
# 3 3 3
