from itertools import islice, count
from common.polygonal import pentagonal
from common.logging import info


def gen_pentagonal():
    for i in count(1):
        yield pentagonal(i)


def solve():
    limit = 10000
    p = list(islice(gen_pentagonal(), limit))
    ps = set(p)

    for j in range(1, limit):
        for k in range(j, limit):
            if p[k] - p[j] in ps and p[k] + p[j] in ps:
                info(f"Pk={p[k]}, Pj={p[j]}, Pk-Pj={p[k]-p[j]}, Pk+Pj={p[k]+p[j]}")
                return p[k] - p[j]


if __name__ == "__main__":
    print(solve())
