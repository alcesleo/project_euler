"""Mathematical operations not covered by the standard library math functions."""

import functools


def factors(n):
    """Return all the factors of n as a set.

    >>> factors(15)
    {1, 3, 5, 15}
    """
    result = set()

    # Each factor below sqrt(n) will have a matching factor above sqrt(n) - n / i
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)

    return result


@functools.lru_cache(maxsize=2048)
def partitions(n, numbers=None):
    """Return the amount of partitions of n into numbers, a tuple sorted from biggest to smallest."""
    if numbers == None:
        numbers = tuple(reversed(range(1, n + 1)))
        return partitions(n, numbers)

    if len(numbers) == 0:
        return 0

    number, *rest = numbers
    most = n // number
    result = 0

    for count in range(0, most + 1):
        total = number * count
        remainder = n - total

        if total == n and count != 0:
            result += 1

        result += partitions(remainder, tuple(rest))

    return result


@functools.lru_cache(maxsize=256)
def proper_divisors(n):
    """The proper divisors of n are its factors other than itself

    >>> proper_divisors(10)
    {1, 2, 5}

    >>> proper_divisors(2)
    {1}
    """
    return factors(n) - {n}


def phi(n):
    """Return the Euler's Totient of n, i.e. the number of relative primes to n below n.

    https://www.geeksforgeeks.org/eulers-totient-function/
    """
    result = n
    p = 2

    while(p * p <= n):
        if (n % p == 0):
            while (n % p == 0):
                n //= p

            result -= result // p

        p += 1

    if (n > 1):
        result -= result // n

    return result


def is_palindrome(n):
    """Return whether a n is a palindrome.

    >>> is_palindrome(12321)
    True

    >>> is_palindrome(123210)
    False

    >>> is_palindrome("racecar")
    True
    """
    n = str(n)
    reverse = n[::-1]
    return n == reverse
