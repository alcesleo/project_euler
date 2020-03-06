import itertools
from common.primes import gen_primes, is_prime

limit = 10_000
PRIMES = list(itertools.takewhile(lambda n: n < limit, gen_primes()))


def is_twice_square(n):
    """Returns whether n is twice a square

    >>> is_twice_square(2 * (3 ** 2))
    True

    >>> is_twice_square(2 * (4 ** 2))
    True
    """
    return ((n / 2) ** 0.5).is_integer()


def is_prime_plus_twice_square(n):
    """Returns whetner n can be written as a prime plus two times a square
    """
    for prime in PRIMES:
        if prime >= i:
            break

        if is_twice_square(i - prime):
            return True

    return False


for i in range(3, limit, 2):
    if is_prime(i):
        continue

    if not is_prime_plus_twice_square(i):
        print(i)
        break
