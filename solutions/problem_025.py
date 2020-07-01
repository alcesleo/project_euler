def gen_fibonacci():
    a, b = 1, 1

    while True:
        yield a
        a, b = b, a + b


def solve(limit):
    """
    >>> solve(3)
    12
    """
    for i, n in enumerate(gen_fibonacci(), 1):
        if len(str(n)) >= limit:
            return i

if __name__ == "__main__":
    print(solve(1000))
