import itertools
from common.primes import gen_primes, is_prime

LIMIT = 1_000_000

primes = list(itertools.takewhile(lambda p: p < LIMIT, gen_primes()))

longest = 0
result = 0

for start in range(0, len(primes)):
    prime_slice = primes[start:]
    total = 0

    for length, prime in enumerate(prime_slice, 1):
        total += prime

        if total >= LIMIT:
            break

        if length > longest and is_prime(total):
            longest = length
            result = total

print(result)
