from collections import Counter


def duplicate_count(text):
    # big O(n) complexity
    counts = Counter(text.lower())

    return len([char for char, count in counts.items() if count > 1])
