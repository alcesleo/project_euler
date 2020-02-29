from itertools import permutations
from common.tools import digits_to_int

pandigital = list(range(10))
result = 0

for permutation in permutations(pandigital):
    if digits_to_int(permutation[1:4]) % 2 != 0:
        continue

    if digits_to_int(permutation[2:5]) % 3 != 0:
        continue

    if digits_to_int(permutation[3:6]) % 5 != 0:
        continue

    if digits_to_int(permutation[4:7]) % 7 != 0:
        continue

    if digits_to_int(permutation[5:8]) % 11 != 0:
        continue

    if digits_to_int(permutation[6:9]) % 13 != 0:
        continue

    if digits_to_int(permutation[7:10]) % 17 != 0:
        continue

    result += digits_to_int(permutation)


print(result)
