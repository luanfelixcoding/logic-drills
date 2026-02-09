"""
Codewars Challenge: Split Strings
Rank: 5 kyu
URL: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
"""


def solution(s):
    if len(s) % 2 != 0:
        s = s + "_"

    result = []

    for i in range(0, len(s), 2):
        pair = s[i: i+2]
        result.append(pair)

    return result
