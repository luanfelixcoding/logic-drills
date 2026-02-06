"""
Codewars Challenge: Break camelCase
Rank: 6 kyu
URL: https://www.codewars.com/kata/5208f99aee097e6552000148
"""


def solution(s):
    return "".join(" " + char if char.isupper() else char for char in s)


print(solution("camelCasing"))  # camel Casing
print(solution("giveMeAStar"))  # give Me A Star
