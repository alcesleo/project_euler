from itertools import takewhile
from common.primes import gen_primes

LIMIT = 2_000_000

result = sum(takewhile(lambda x: x < LIMIT, gen_primes()))
print(result)
