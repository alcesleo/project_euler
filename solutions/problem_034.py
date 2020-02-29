from math import factorial
from common.tools import digits


def digit_factorial(n):
    return sum(map(factorial, digits(n)))


result = 0
limit = 50_000

for n in range(3, limit):
    if n == digit_factorial(n):
        result += n

print(result)
