import itertools


def gen_primes():
    """
    Generates an infinite sequence of prime numbers.

    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
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
            # It's a composite number, mark the next multiples as prime factors
            for factor in composites[number]:
                composites.setdefault(factor + number, []).append(factor)

            # When the algorithm passes this number, it is no longer needed in this list
            del composites[number]

        number += 1
