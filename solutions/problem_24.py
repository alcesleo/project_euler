import itertools

TARGET = 1_000_000
DIGITS = list(range(10))

permutations = itertools.permutations(DIGITS)
permutation = next(itertools.islice(permutations, TARGET - 1, None))
result = "".join([str(n) for n in permutation])

print(result)
