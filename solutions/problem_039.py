from math import sqrt
from common.logging import info

def pythagorean_perimeters(limit):
    """Returns a dict of perimeters mapped to sets of their corresponding
    pythagorean triplets up to a limit.
    """
    perimeters = {}

    for a in range(1, limit):
        for b in range(a, limit):
            c = sqrt(a**2 + b**2)

            if not c.is_integer():
                continue

            c = int(c)
            perimeter = a + b + c

            if perimeter > limit:
                break

            perimeters.setdefault(perimeter, set()).add((a, b, c))

    return perimeters


def solve(limit):
    """
    >>> solve(150)
    """
    solutions = pythagorean_perimeters(limit)
    max_solutions = 0
    max_perimeter = 0

    for perimeter, solutions in solutions.items():
        if len(solutions) > max_solutions:
            info(f"p={perimeter}, {len(solutions)} solutions, {solutions}")
            max_perimeter = perimeter
            max_solutions = len(solutions)

    return max_perimeter


if __name__ == "__main__":
    print(solve(1000))
