"""
Codewars Challenge: Replace With Alphabet Position
Rank: 6 kyu
URL: https://www.codewars.com/kata/546f922b54af40e1e90001da
"""


def alphabet_position(text: str):
    numbers = [str(ord(char.lower()) - 96) for char in text if char.isalpha()]

    return " ".join(numbers)


# 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
print(alphabet_position("The sunset sets at twelve o' clock."))
