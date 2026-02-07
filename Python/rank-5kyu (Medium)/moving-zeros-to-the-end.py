"""
Codewars Challenge: Break camelCase
Rank: 5 kyu
URL: https://www.codewars.com/kata/52597aa56021e91c93000cb0
"""


def move_zeros(lst: list):
    no_zero = [num for num in lst if num != 0]
    zeros = [num for num in lst if num == 0]

    return no_zero + zeros


# [13, 23, 43, 53, 0, 0, 0, 0]
print(move_zeros([0, 13, 23, 0, 0, 0, 43, 53]))

# [9, 7, 4, 6, 1, 99, 0, 0, 0, 0, 0]
print(move_zeros([9, 0, 7, 0, 4, 0, 6, 0, 1, 0, 99]))
