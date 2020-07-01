SIDES = 4

def solve(width):
    """
    >>> solve(5)
    101
    """
    n = 1
    step = 2
    sum_diagonals = 1

    while n < width * width:
        for i in range(SIDES):
            n += step
            sum_diagonals += n

        step += 2

    return sum_diagonals


if __name__ == "__main__":
    print(solve(1001))
