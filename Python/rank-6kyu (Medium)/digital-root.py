"""
Codewars Challenge: Digital Root
Rank: 6 kyu
URL: https://www.codewars.com/kata/541c8630095125aba6000c00
"""


def digital_root(n):
    if n < 10:
        return n

    n = sum(int(digit) for digit in str(n))
    return digital_root(n)
