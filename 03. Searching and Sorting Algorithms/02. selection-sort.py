nums = [int(x) for x in input().split()]

for idx in range(len(nums)):
    min_idx = idx
    for curr_idx in range(idx + 1, len(nums)):
        if nums[curr_idx] < nums[min_idx]:
            min_idx = curr_idx
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(*nums)


# Description:
# Write an implementation of Selection Sort. You should read an array of integers and sort them.
#
# Output:
# • You should print out the sorted list in the format described below.
#
#
# Examples:
#
# Input:
# 5 4 3 2 1
#
# Expected output:
# 1 2 3 4 5
#
#
# Input:
# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86
#
# Expected output:
# 5 7 7 10 13 14 15 16 17 17 21 27 28 31 32 34 36 37 38 42 52 55 61 65 65 65 68 70 74 86 86 86 89 93 93 96 97
