from functools import lru_cache


@lru_cache(maxsize=2048)
def partitions(n, numbers=None):
    """Returns the amount of partitions of n into a set of numbers
    """
    if numbers == None:
        numbers = tuple(reversed(range(1, n + 1)))
        return partitions(n, numbers)

    if len(numbers) == 0:
        return 0

    number, *rest = numbers
    most = n // number
    result = 0

    for count in range(0, most + 1):
        total = number * count
        remainder = n - total

        if total == n and count != 0:
            result += 1

        result += partitions(remainder, tuple(rest))

    return result


def solve():
    target = 200
    coins = (200, 100, 50, 20, 10, 5, 2, 1)

    return partitions(target, coins)


if __name__ == "__main__":
    print(solve())
