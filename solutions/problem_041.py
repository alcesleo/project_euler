from itertools import permutations
from common.primes import is_prime
from common.digits import join_digits

largest_pandigital_prime = 0

for n in range(1, 10):
    digits = set(range(1, n + 1))

    for c in permutations(digits):
        candidate = join_digits(c)

        if is_prime(candidate):
            largest_pandigital_prime = candidate

print(largest_pandigital_prime)
