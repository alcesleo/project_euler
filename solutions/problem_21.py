from common.tools import factors
from functools import lru_cache


@lru_cache(maxsize=256)
def proper_divisors(n):
    """The proper divisors of n are its factors other than itself
    """
    return factors(n) - {n}


@lru_cache(maxsize=256)
def is_amicable(a, b):
    return a != b and sum(proper_divisors(a)) == b and sum(proper_divisors(b)) == a


LIMIT = 10_000

result = 0
for a in range(1, LIMIT):
    for b in range(a, LIMIT):
        if is_amicable(a, b):
            result += a + b

print(result)
