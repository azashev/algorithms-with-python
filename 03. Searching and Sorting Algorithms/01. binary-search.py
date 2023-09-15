# nums = [int(x) for x in input().split()]
# target = int(input())
#
#
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         mid_el = numbers[mid]
#         if mid_el == target:
#             return mid
#
#         if mid_el < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return - 1
#
#
# print(binary_search(nums, target))


# Using recursion:
nums = [int(x) for x in input().split()]
target = int(input())
left = 0
right = len(nums) - 1


def binary_search(numbers, target, left, right):
    if left > right:
        return - 1

    mid = (left + right) // 2
    mid_el = numbers[mid]
    if mid_el == target:
        return mid

    if mid_el < target:
        return binary_search(numbers, target, mid + 1, right)
    else:
        return binary_search(numbers, target, left, mid - 1)


print(binary_search(nums, target, left, right))


# Description
# Implement an algorithm that finds the index of an element in a sorted array of integers in logarithmic time.
#
# Examples:
#
# Input:
# 1 2 3 4 5
# 1
#
# Expected output:
# 0
#
#
#
# Input:
# -1 0 1 2 4
# 1
#
# Expected output:
# 2
