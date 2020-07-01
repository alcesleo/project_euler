from itertools import permutations
from common.tools import nth
from common.digits import join_digits


def solve(target):
    digits = list(range(10))
    permutation = nth(permutations(digits), target)

    return join_digits(permutation)


if __name__ == "__main__":
    print(solve(1_000_000))
