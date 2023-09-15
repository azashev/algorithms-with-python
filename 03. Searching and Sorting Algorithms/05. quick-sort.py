def quick_sort(start, end, numbers):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if numbers[left] > numbers[pivot] > numbers[right]:
            numbers[left], numbers[right] = numbers[right], numbers[left]
        if numbers[left] <= numbers[pivot]:
            left += 1
        if numbers[right] >= numbers[pivot]:
            right -= 1

    numbers[pivot], numbers[right] = numbers[right], numbers[pivot]
    quick_sort(start, right - 1, numbers)
    quick_sort(left, end, numbers)


nums = [int(x) for x in input().split()]

quick_sort(0, len(nums) - 1, nums)

print(*nums)

# Description:
# Sort an array of elements using quicksort.
#
# Example:
#
# Input:
# 5 4 3 2 1
#
# Expected output:
# 1 2 3 4 5
