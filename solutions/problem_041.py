from common.primes import is_prime
from common.tools import digits_to_int
from itertools import permutations

largest_pandigital_prime = 0

for n in range(1, 10):
    digits = set(range(1, n + 1))

    for c in permutations(digits):
        candidate = digits_to_int(c)

        if is_prime(candidate):
            largest_pandigital_prime = candidate

print(largest_pandigital_prime)
