"""
Codewars Challenge: Bouncing Balls
Rank: 6 kyu
URL: https://www.codewars.com/kata/5544c7a5cb454edb3c000047
"""


def bouncing_ball(h, bounce, window):
    # your code
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1

    count = 1

    current_height = h * bounce

    while current_height > window:
        count += 2
        current_height *= bounce

    return count
