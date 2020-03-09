import itertools
from common.tools import nth, join_digits

TARGET = 1_000_000
DIGITS = list(range(10))

permutations = itertools.permutations(DIGITS)
permutation = nth(permutations, TARGET)
result = join_digits(permutation)

print(result)
