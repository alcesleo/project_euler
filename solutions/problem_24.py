import itertools
from common.tools import nth

TARGET = 1_000_000
DIGITS = list(range(10))

permutations = itertools.permutations(DIGITS)
permutation = nth(permutations, TARGET)
result = "".join([str(n) for n in permutation])

print(result)
