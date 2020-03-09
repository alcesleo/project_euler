from math import factorial
from common.tools import split_digits


def digit_factorial(n):
    return sum(map(factorial, split_digits(n)))


result = 0
limit = 50_000

for n in range(3, limit):
    if n == digit_factorial(n):
        result += n

print(result)
