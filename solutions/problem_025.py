import itertools


def gen_fibonacci():
    a, b = 1, 1

    while True:
        yield a
        a, b = b, a + b


LIMIT = 1000

for i, n in enumerate(gen_fibonacci(), 1):
    if len(str(n)) >= LIMIT:
        print(i)
        break
