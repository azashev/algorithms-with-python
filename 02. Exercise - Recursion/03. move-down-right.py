def count_all_paths(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += count_all_paths(row, col + 1, rows, cols)
    result += count_all_paths(row + 1, col, rows, cols)

    return result


rows = int(input())
cols = int(input())

print(count_all_paths(0, 0, rows, cols))

# Description
#
# Marinette has the ability to transform into Ladybug. She is stuck on a grid. Her initial location is in the top-left
# corner and tries to move to the bottom-right corner. However, she can only move either down or right at any point
# in time.
# Write a program that prints the number of all possible unique paths that Marinette can take to reach the bottom-right
# corner.
#
# • On the first line you will receive an integer – m – number of rows.
# • On the second line you will receive an integer – n – number of cols.
# • Print the number of all possible unique paths to the bottom-right corner.
#
# Constraints:
# m and n will always be in the range 0 to 1000
#
#
# Examples:
#
# Input:
# 3
# 2
#
# Expected output:
# 3
#
#
# Input:
# 3
# 5
#
#
# All possible unique paths:
# -------------
# | Start | X |
# -------------
# |       | X |
# -------------
# |       | X |
# -------------
#
#
#
# -------------
# | Start |   |
# -------------
# |   X   | X |
# -------------
# |       | X |
# -------------
#
#
#
# -------------
# | Start |   |
# -------------
# |   X   |   |
# -------------
# |   X   | X |
# -------------
#
