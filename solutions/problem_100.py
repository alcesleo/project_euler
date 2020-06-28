"""
We want to find integer solutions to the following equation:

    x/y * (x-1)/(y-1) = 1/2

We can start by rewriting it a bit:

    x(x-1)      / y(y-1)    = 1/2
    (x^2 - x)   / (y^2 - y) = 1/2
    (2x^2 - 2x) / (y^2 - y) = 1
    2x^2 - 2x               = y^2 - y
    2x^2 - 2x - y^2 + y     = 0

Now it's starting to look a lot like a Diophantine equation as encountered in
problem 66. Some basic algebra I can do, but I would have been screwed here if
it weren't for finding this website:

https://www.alpertron.com.ar/QUAD.HTM

When plugging in this equation it provides a recursive solution, I can't claim
to understand the dark magic behind it.

    x[n+1] = 3x[n] + 2y[n] - 2
    y[n+1] = 4x[n] + 3y[n] - 3
"""

from fractions import Fraction
from common.logging import info

def solve(target):
    """
    >>> solve(20)
    15

    >>> solve(100)
    85
    """

    blue, discs = 1, 1

    while discs < target:
        blue, discs = 3*blue + 2*discs - 2,\
                      4*blue + 3*discs - 3

        probability = Fraction(blue, discs) * Fraction(blue-1, discs-1)
        info(f"P(BB) = {blue}/{discs} * {blue-1}/{discs-1} = {probability}")

    return blue



if __name__ == "__main__":
    print(solve(10**12))
