def solve(limit):
    """
    >>> solve(10)
    23
    """
    total = 0

    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0:
            total += x

    return total

if __name__ == "__main__":
    print(solve(1000))
