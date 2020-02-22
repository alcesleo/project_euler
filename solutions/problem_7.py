import itertools
from common import primes

TARGET = 10_001

nth_prime = next(itertools.islice(primes.gen_primes(), TARGET - 1, None))

print(nth_prime)
