def recursive_fact(num):
    if num <= 1:
        return 1
    return num * recursive_fact(num - 1)


number = int(input())
print(recursive_fact(number))

# Description:
# Write a program that calculates the recursively factorial of a given number.
#
#
# Examples:
#
# Input:
# 5
#
# Expected output:
# 120
#
#
# Input:
# 10
#
# Expected output:
# 3628800
