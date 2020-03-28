"""
https://en.wikipedia.org/wiki/E_(mathematical_constant)
https://en.wikipedia.org/wiki/Continued_fraction
"""
from fractions import Fraction
from itertools import count, islice
from common.digits import sum_digits


def continued_fraction(a0, a):
    """Given the terms of a continued fraction in the form [a0; a1, a2, a3, a4 ...], return the convergent after expanding all terms as a Fraction.

    https://en.wikipedia.org/wiki/Continued_fraction

    # Equivalent to the following recursive expansions
    from fractions import Fraction as F
    a0
    a0 + F(1, a[0])
    a0 + F(1, a[0] + F(1, a[1]))
    a0 + F(1, a[0] + F(1, a[1] + F(1, a[2])))
    a0 + F(1, a[0] + F(1, a[1] + F(1, a[2] + F(1, a[3]))))
    a0 + F(1, a[0] + F(1, a[1] + F(1, a[2] + F(1, a[3] + F(1, a[4])))))

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
    return a0 + converge(a)


def converge(terms):
    """Recursive fraction given a finite list of terms.

    >>> converge([])
    Fraction(0, 1)

    >>> converge([1])
    Fraction(1, 1)

    >>> converge([1, 2])
    Fraction(2, 3)

    >>> converge([1, 2, 1])
    Fraction(3, 4)

    >>> converge([1, 2, 1, 1])
    Fraction(5, 7)

    >>> converge([1, 2, 1, 1, 4])
    Fraction(23, 32)
    """
    if not terms:
        return Fraction(0, 1)

    a, *ak = terms
    return Fraction(1, a + converge(ak))


def gen_terms_e():
    """Yields the terms of the continued fraction for e.

    https://oeis.org/A003417

    >>> list(islice(gen_terms_e(), 20))
    [1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14]
    """
    for i in count():
        if i % 3 == 1:
            yield 2 * (1 + i//3)
        else:
            yield 1


def solve(target=10):
    terms = islice(gen_terms_e(), target - 1)
    convergent = continued_fraction(2, terms)

    return sum_digits(convergent.numerator)


if __name__ == "__main__":
    print(solve(100))
