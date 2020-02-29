
def pythagorean_perimeters(limit):
    """Returns a dict of perimeters mapped to sets of their corresponding pythagorean triplets up to a limit
    """
    perimeters = {}

    for a in range(1, limit):
        for b in range(a, limit):
            c = (a**2 + b**2) ** 0.5

            if not c.is_integer():
                continue

            c = int(c)
            perimeter = a + b + c

            if perimeter > limit:
                break

            perimeters.setdefault(perimeter, set()).add((a, b, c))

    return perimeters


LIMIT = 1000

solutions = pythagorean_perimeters(LIMIT)
maximum_solutions = 0
maximum_perimeter = 0

for perimeter, solutions in solutions.items():
    if len(solutions) > maximum_solutions:
        maximum_perimeter = perimeter
        maximum_solutions = len(solutions)

print(maximum_perimeter)
