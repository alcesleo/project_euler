from common.math import partitions


def solve():
    target = 200
    coins = (200, 100, 50, 20, 10, 5, 2, 1)

    return partitions(target, coins)


if __name__ == "__main__":
    print(solve())
