from math import factorial


def count_combinations(n, r):
    """Returns the number of combinations for n over r

    >>> count_combinations(5, 3)
    10

    >>> count_combinations(23, 10)
    1144066
    """
    return factorial(n) // (factorial(r) * factorial(n - r))


LIMIT = 100
TARGET = 1_000_000
result = 0

for n in range(1, LIMIT + 1):
    for r in range(1, n + 1):
        if count_combinations(n, r) > TARGET:
            result += 1

print(result)
