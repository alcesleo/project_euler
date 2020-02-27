from common import primes
from itertools import takewhile

LIMIT = 2_000_000

result = sum(takewhile(lambda x: x < LIMIT, primes.gen_primes()))

print(result)
