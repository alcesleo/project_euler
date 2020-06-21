from itertools import takewhile
from math import sqrt
from common.primes import gen_primes

def largest_prime_factor(n):
    """
    >>> largest_prime_factor(13195)
    29
    """
    largest_factor = 0
    limit = sqrt(n)

    for p in takewhile(lambda p: p < limit, gen_primes()):
        if n % p == 0:
            largest_factor = p

    return largest_factor

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
