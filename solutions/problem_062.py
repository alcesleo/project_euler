from collections import defaultdict
from itertools import count
from common.digits import split_digits


def gen_cubes():
    for i in count(1):
        yield i ** 3


def solve(target=3):
    cubes = defaultdict(list)

    for c in gen_cubes():
        key = tuple(sorted(split_digits(c)))
        cubes[key].append(c)

        if len(cubes[key]) >= target:
            return min(cubes[key])


if __name__ == "__main__":
    print(solve(5))
