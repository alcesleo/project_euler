from functools import lru_cache
from common.math import proper_divisors

LIMIT = 10_000


@lru_cache(maxsize=LIMIT)
def sum_proper_divisors(n):
    return sum(proper_divisors(n))


def is_amicable(a, b):
    return a != b and sum_proper_divisors(a) == b and sum_proper_divisors(b) == a


result = 0
for a in range(1, LIMIT):
    for b in range(a, LIMIT):
        if is_amicable(a, b):
            result += a + b

print(result)
