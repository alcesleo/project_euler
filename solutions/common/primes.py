import itertools


def gen_primes():
    """
    Generates an infinite sequence of prime numbers.

    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> list(itertools.islice(gen_primes(), 10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """

    composites = {}  # A dict of composite numbers mapped to a list of their factors
    number = 2   # The number being checked for primeness

    while True:
        if number not in composites:
            # If it's not a composite number, it is a prime
            yield number

            # Add this number as a prime factor of the first multiple of it
            composites[number * number] = [number]
        else:
            # If it's a composite number, mark factors of its composites
            for factor in composites[number]:
                composites.setdefault(factor + number, []).append(factor)

            # When the algorithm passes this number, it is no longer needed in this list
            del composites[number]

        number += 1


def is_prime(n):
    """Returns whether n is prime

    >>> is_prime(29)
    True

    >>> is_prime(28)
    False
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
