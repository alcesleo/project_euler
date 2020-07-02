from itertools import permutations
from common.primes import is_prime
from common.digits import join_digits


def solve():
    largest_pandigital_prime = 0

    for n in range(1, 10):
        digits = set(range(1, n + 1))

        for c in permutations(digits):
            candidate = join_digits(c)

            if is_prime(candidate):
                largest_pandigital_prime = candidate

    return largest_pandigital_prime


if __name__ == "__main__":
    print(solve())
