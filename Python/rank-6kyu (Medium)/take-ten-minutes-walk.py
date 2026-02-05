"""
Codewars Challenge: Take a Ten Minutes Walk
Rank: 6 kyu
URL: https://www.codewars.com/kata/54da539698b8a2ad76000228
"""


def is_valid_walk(walk):
    # determine if walk is valid
    if len(walk) != 10:
        return False

    # here we need to check if the same amount of north is equal to south
    # same to east and west in order to annul each other
    return walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
