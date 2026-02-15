"""
Codewars Challenge: Simple Pig Latin
Rank: 5 kyu
URL: https://www.codewars.com/kata/520b9d2ad5c005041100000f
"""


def pig_it(text: str):
    # your code here
    words = text.split()
    result = []

    for word in words:
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
            result.append(new_word)
        else:
            result.append(word)
    return " ".join(result)


print(pig_it('Pig latin is cool !'))
