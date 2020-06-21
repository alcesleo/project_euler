def solve(limit):
    """
    >>> solve(100)
    44
    """
    total = 0
    a, b = 0, 1

    while a < limit:
        if (a % 2 == 0):
            total += a

        a, b = b, a + b

    return total

if __name__ == "__main__":
    print(solve(4_000_000))
