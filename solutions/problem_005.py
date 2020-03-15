from functools import reduce
from math import gcd

LIMIT = 20


def lcm(a, b):
    return a * b // gcd(a, b)


def lcms(*numbers):
    return reduce(lcm, numbers)


result = lcms(*range(1, LIMIT))
print(result)
