from itertools import takewhile
from collections import deque
from common.tools import digits, digits_to_int
from common.primes import gen_primes, is_prime


def rotations(n):
    d = deque(digits(n))
    result = []

    for i in range(len(d)):
        result.append(digits_to_int(d))
        d.rotate()

    return result


LIMIT = 1_000_000
primes = takewhile(lambda n: n < LIMIT, gen_primes())
count = 0

for p in primes:
    if all(map(is_prime, rotations(p))):
        count += 1

print(count)
