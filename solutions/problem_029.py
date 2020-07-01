def solve(limit):
    """
    >>> solve(5)
    15
    """
    numbers = set()

    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            numbers.add(a ** b)

    return len(numbers)

if __name__ == "__main__":
    print(solve(100))
