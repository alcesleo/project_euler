from math import sqrt
from itertools import combinations, product


def distance(p1, p2):
    """Returns the distance between 2 points in 2d.

    > The distance between (x1, y1) and (x2, y2) is given by:
    > d = sqrt((x2 - x1)^2 + (y2 -y1)^2)

    - https://en.wikipedia.org/wiki/Distance
    """
    x1, y1 = p1
    x2, y2 = p2

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def is_right_triangle(o, p, q, precision=10):
    """Returns whether 3 given points form a right triangle.

    https://en.wikipedia.org/wiki/Pythagorean_theorem
    """
    a, b, c = sorted((
        distance(o, p),
        distance(o, q),
        distance(p, q)))

    return round(a**2 + b**2, precision) == round(c**2, precision)


def solve(size=2):
    coordinates = list(product(range(size + 1), repeat=2))

    o = (0, 0)
    coordinates.remove(o)

    right_triangles = 0

    for p, q in combinations(coordinates, 2):
        if is_right_triangle(o, p, q):
            right_triangles += 1

    return right_triangles


if __name__ == "__main__":
    print(solve(50))
