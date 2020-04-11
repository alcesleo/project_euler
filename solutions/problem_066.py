"""
I thought I was being quite clever at first by sieving through values of y^2 + 1
which would always yield a solution for x, and simply saving the x in d_min_x if
it's smaller than the existing value.

    d_min_x = {}

    for d in range(1, limit_d + 1):
        for y in range(1, limit_y + 1):
            x2 = d * (y**2) + 1

The problem here is limit_y which you have to crank up to ludicrous numbers to get a solution for some D.

After reading up on Diophantine equations on Wikipedia, it turns out the equation
in this problem is known as Pell's equation, for which you can get a minimal solution
by plugging in the numerator and denominator of the convergents of √D:

> Thus, the fundamental solution may be found by performing the continued fraction expansion
> and testing each successive convergent until a solution to Pell's equation is found.

https://en.wikipedia.org/wiki/Diophantine_equation
https://en.wikipedia.org/wiki/Pell%27s_equation
"""

from math import sqrt
from itertools import cycle

from common.continued_fractions import continued_fraction
from common.logging import info, debug
from solutions.problem_064 import period_of_root


def convergents_of_root(n):
    """Yields the (numerator, denominator) of each successive convergent of √n
    """
    a0, *period = period_of_root(n)
    a = ()

    for an in cycle(period):
        f = continued_fraction(a0, a)
        yield (f.numerator, f.denominator)
        a = a + (an,)


def pells_equation(d):
    """Finds the minimal solution for x in Pell's equation x^2 – Dy^2 = 1 and returns (x, y)

    # 9^2 – 5*4^2 = 1
    >>> pells_equation(5)
    (9, 4)

    # 8^2 – 7*3^2 = 1
    >>> pells_equation(7)
    (8, 3)
    """
    for x, y in convergents_of_root(d):
        if x*x - d*y*y == 1:
            return x, y


def square(n):
    return sqrt(n).is_integer()


def solve(limit=7):
    d_min_x = {}

    for d in range(limit + 1):
        if square(d):
            continue

        x, y = pells_equation(d)
        d_min_x[d] = x

        debug(f"{x}^2 - {d}*{y}^2 = {(x**2) - (d*y*y)}")

    result = max(d_min_x, key=lambda k: d_min_x[k])
    info(f"D={result}, x={d_min_x[d]}")

    return result


if __name__ == "__main__":
    print(solve(1000))
