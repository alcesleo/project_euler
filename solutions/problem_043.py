from itertools import permutations
from common.digits import join_digits

def solve():
    pandigital = list(range(10))
    result = 0

    for permutation in permutations(pandigital):
        if join_digits(permutation[1:4]) % 2 != 0:
            continue

        if join_digits(permutation[2:5]) % 3 != 0:
            continue

        if join_digits(permutation[3:6]) % 5 != 0:
            continue

        if join_digits(permutation[4:7]) % 7 != 0:
            continue

        if join_digits(permutation[5:8]) % 11 != 0:
            continue

        if join_digits(permutation[6:9]) % 13 != 0:
            continue

        if join_digits(permutation[7:10]) % 17 != 0:
            continue

        result += join_digits(permutation)

    return result


if __name__ == "__main__":
    print(solve())
