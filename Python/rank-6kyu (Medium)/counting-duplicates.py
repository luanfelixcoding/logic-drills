"""
Codewars Challenge: Counting Duplicates
Rank: 6 kyu
URL: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
"""

from collections import Counter


def duplicate_count(text):
    # big O(n) complexity
    counts = Counter(text.lower())

    return len([char for char, count in counts.items() if count > 1])
