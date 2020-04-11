"""Expands continued fractions.

See https://en.wikipedia.org/wiki/Continued_fraction for example notations and terminology.
"""

from math import sqrt
from fractions import Fraction
from functools import lru_cache


def continued_fraction(a0, a):
    """Given the terms of a continued fraction in the form [a0; a1, a2, a3, a4 ...], return the convergent after expanding all terms of `a` as a Fraction.

    This is equivalent to the following:

    from fractions import Fraction as F
    a0
    a0 + F(1, a[0])
    a0 + F(1, a[0] + F(1, a[1]))
    a0 + F(1, a[0] + F(1, a[1] + F(1, a[2])))
    a0 + F(1, a[0] + F(1, a[1] + F(1, a[2] + F(1, a[3]))))
    a0 + F(1, a[0] + F(1, a[1] + F(1, a[2] + F(1, a[3] + F(1, a[4])))))
    ...

    >>> continued_fraction(2, [])
    Fraction(2, 1)

    >>> continued_fraction(2, [1])
    Fraction(3, 1)

    >>> continued_fraction(2, [1, 2])
    Fraction(8, 3)

    >>> continued_fraction(2, [1, 2, 1])
    Fraction(11, 4)

    >>> continued_fraction(2, [1, 2, 1, 1])
    Fraction(19, 7)

    >>> continued_fraction(2, [1, 2, 1, 1, 4])
    Fraction(87, 32)

    >>> continued_fraction(2, [1, 2, 1, 1, 4, 1])
    Fraction(106, 39)
    """
    return a0 + converge(tuple(a))


@lru_cache()
def converge(terms):
    """Recursive fraction given a finite list of terms.

    >>> converge(())
    Fraction(0, 1)

    >>> converge((1,))
    Fraction(1, 1)

    >>> converge((1, 2))
    Fraction(2, 3)

    >>> converge((1, 2, 1))
    Fraction(3, 4)

    >>> converge((1, 2, 1, 1))
    Fraction(5, 7)

    >>> converge((1, 2, 1, 1, 4))
    Fraction(23, 32)
    """
    if not terms:
        return Fraction(0, 1)

    return Fraction(1, terms[0] + converge(terms[1:]))


def period_of_root(n):
    """Returns [a0, a1, a2, a3, ..., an] for the square root of n,
    where a1...an is the repeating period as denoted in the format [a0; (a1, a2, a3, ..., an)].

    This is just a Python port of the C++ code in the accepted answer:

    https://stackoverflow.com/questions/12182701/generating-continued-fractions-for-square-roots
    """
    r = int(sqrt(n))

    result = [r]

    if (r * r == n):
        return result

    a = r
    p = 0
    q = 1

    while True:
        p = a * q - p
        q = (n - p*p) // q
        a = (r + p) // q

        result.append(a)

        if q == 1:
            break

    return result
