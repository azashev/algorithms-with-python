def calc_sum(numbers, idx):
    if idx >= len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + calc_sum(numbers, idx + 1)


nums = [int(x) for x in input().split(' ')]
print(calc_sum(nums, 0))

# Description:
# Write a program that finds the sum of all elements in an integer array. Use recursion.

# Example
#
# Input:
# 1 2 3 4
#
# Expected output:
# 10
#
#
# Input:
# -1 0 1
#
# Expected output:
# 0
