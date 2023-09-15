nums = [int(x) for x in input().split()]

for idx in range(1, len(nums)):
    for j in range(idx, 0, -1):
        if nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        else:
            break

print(*nums)


# Solution 2:
# nums = [int(x) for x in input().split()]
#
# for i in range(len(nums)):
#     j = i
#     while j > 0 and nums[j] < nums[j - 1]:
#         nums[j], nums[j - 1] = nums[j - 1], nums[j]
#         j -= 1
#
# print(*nums)

# Description
#
# Write an implementation of Insertion Sort. You should read an array of integers and sort them.
# Output
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
#
# Input:
# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51
#
# Expected output:
# 5 7 7 10 13 14 15 16 17 17 21 27 28 31 32 34 36 37 38 42 44 51 52 55 61 65 65 65 68 70 74 86 86 86 89 93 93 96 97
