import itertools


def pentagonal(n):
    return n * (3 * n - 1) / 2


def gen_pentagonal():
    for i in itertools.count(1):
        yield pentagonal(i)


limit = 10000
p = list(itertools.islice(gen_pentagonal(), limit))
ps = set(p)

for j in range(1, limit):
    for k in range(j, limit):
        if p[k] - p[j] in ps and p[k] + p[j] in ps:
            print(p[k] - p[j])
