"""
The high limit of a billion left most of my early attempts dead in the
water as even an empty loop up to that number is slow. Fortunately, the
wikipedia page on Heronian Triangles **almost** has the answer, it's a really
simple formula but unfortunately generates (n-1, n, n+1) triangles rather than
the (n, n, n±1) triangles we need.

A bit of experimentation shows that it can be adapted to do what we need, we just
need to alternatingly add or subtract 2 to n, and 1 to the last side of the triangle.

Turns out there are only 14 triangles that fit the requirements and it runs in 0.1s.

https://en.wikipedia.org/wiki/Heronian_triangle#Almost-equilateral_Heronian_triangles
"""

from math import sqrt
from common.logging import info

def triangle_area(a, b, c):
    """Returns the area of a triangle given its 3 sides using Heron's formula."""
    s = (a + b + c) / 2
    return sqrt(s * (s-a) * (s-b) * (s-c))


def solve(limit):
    total = 0

    n_1, n_2, sign = 1, 1, 1

    while True:
        # Calculate the next n given the 2 previous n
        n = n_1 * 4 - n_2 + 2 * sign

        sides = (n, n, n + sign*1)
        perimeter = sum(sides)

        if perimeter > limit:
            break

        total += perimeter
        area = triangle_area(*sides)
        info(f"{sides}, area={area}, perimeter={perimeter}")

        # Move the previous n forward and flip the sign
        n_1, n_2 = n, n_1
        sign *= -1

    return total


if __name__ == "__main__":
    print(solve(1_000_000_000))
