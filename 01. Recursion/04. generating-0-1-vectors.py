def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[idx] = num
        gen01(idx + 1, vector)


n = int(input())
vector = [0] * n

gen01(0, vector)

# Description:
# Generate all n-bit vectors of 0 and 1 in lexicographic order.
#
# Examples:
#
# Input:
# 3
#
# Expected output:
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
#
#
# Input:
# 5
#
# Expected output:
# 00000
# 00001
# 00010
# ...
# 11110
# 11111
