def print_figure(num):
    if num <= 0:
        return

    print('*' * num)

    print_figure(num - 1)

    print('#' * num)


print_figure(int(input()))

# Description:
# Write a program that draws the figure below depending on n.
#
# Examples:
#
# Input:
# 2
#
# Expected output:
# **
# *
# #
# ##
#
#
# Input:
# 5
#
# Expected output:
# *****
# ****
# ***
# **
# *
# #
# ##
# ###
# ####
# #####
