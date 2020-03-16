import itertools
import os
from functools import reduce, lru_cache
from itertools import permutations


def factors(n):
    """
    Returns all the factors of n as a set

    https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

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


@lru_cache(maxsize=256)
def proper_divisors(n):
    """The proper divisors of n are its factors other than itself

    >>> proper_divisors(10)
    {1, 2, 5}

    >>> proper_divisors(2)
    {1}
    """
    return factors(n) - {n}


def phi(n):
    """Returns the Euler's Totient of n, i.e. the number of relative primes to n below n.

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


def split_digits(n):
    """Returns a list of the digits in n

    >>> split_digits(123)
    [1, 2, 3]
    """
    return [int(d) for d in str(n)]


def join_digits(d):
    """Returns an int from concatenating a list of digits

    >>> join_digits([1, 2, 3])
    123

    >>> join_digits([123, 456])
    123456
    """
    return int("".join(map(str, d)))


def digit_permutations(n):
    """Returns all permutations of digits of n

    >>> digit_permutations(123)
    {321, 132, 231, 213, 312, 123}
    """
    return set(map(join_digits, permutations(split_digits(n))))


def nth(iterable, index):
    """Returns the nth 1-index in an iterable
    """
    return next(itertools.islice(iterable, index - 1, None))


def is_palindrome(n):
    """Returns whether a n is a palindrome

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


def debug(*args):
    """Works as the print() function as long as the DEBUG flag is set, otherwise does nothing
    """

    if os.environ.get("DEBUG"):
        print(*args)
