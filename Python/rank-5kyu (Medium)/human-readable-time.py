"""
Codewars Challenge: Human Readable Time
Rank: 5 kyu
URL: https://www.codewars.com/kata/52685f7382004e774f0001f7
"""


def make_readable(seconds):
    hours = seconds // 3600  # 3600 = 60m * 60s
    minutes = (seconds % 3600) // 60
    other_seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{other_seconds:02d}"
