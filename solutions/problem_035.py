from itertools import takewhile
from collections import deque
from common.tools import split_digits, join_digits
from common.primes import gen_primes, is_prime


def rotations(n):
    d = deque(split_digits(n))
    result = []

    for i in range(len(d)):
        result.append(join_digits(d))
        d.rotate()

    return result


LIMIT = 1_000_000
primes = takewhile(lambda n: n < LIMIT, gen_primes())
count = 0

for p in primes:
    if all(map(is_prime, rotations(p))):
        count += 1

print(count)
