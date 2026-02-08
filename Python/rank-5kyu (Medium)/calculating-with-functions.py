"""
Codewars Challenge: Calculating with Functions
Rank: 5 kyu
URL: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
"""


def zero(func=None): return 0 if func is None else func(0)
def one(func=None): return 1 if func is None else func(1)
def two(func=None): return 2 if func is None else func(2)
def three(func=None): return 3 if func is None else func(3)
def four(func=None): return 4 if func is None else func(4)
def five(func=None): return 5 if func is None else func(5)
def six(func=None): return 6 if func is None else func(6)
def seven(func=None): return 7 if func is None else func(7)
def eight(func=None): return 8 if func is None else func(8)
def nine(func=None): return 9 if func is None else func(9)


def plus(n2): return lambda n1: n1 + n2
def minus(n2): return lambda n1: n1 - n2
def times(n2): return lambda n1: n1 * n2
def divided_by(n2): return lambda n1: n1 // n2


print(seven(times(five())))     # must return 35
print(four(plus(nine())))  # must return 13
print(eight(minus(three())))  # must return 5
print(six(divided_by(two())))  # must return 3
