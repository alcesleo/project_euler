import itertools
from common.polygonal import pentagonal


def gen_pentagonal():
    for i in itertools.count(1):
        yield pentagonal(i)


limit = 10000
p = list(itertools.islice(gen_pentagonal(), limit))
ps = set(p)


def solve():
    for j in range(1, limit):
        for k in range(j, limit):
            if p[k] - p[j] in ps and p[k] + p[j] in ps:
                return p[k] - p[j]


if __name__ == "__main__":
    print(solve())
