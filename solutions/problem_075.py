"""To rephrase this problem, we need to find all Pythagorean triplets whose perimeter is unique.

Wikipedia states that a version of Euclid's formula generates all Pythagorean triples uniquely,
and the formula is quite simple - the tricky part was generating the inputs m, n, and k
to it such that none are missed.

https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
https://www.youtube.com/watch?v=QJYmyhnaaek
"""

from math import gcd
from collections import defaultdict
from itertools import count


def coprime(a, b):
    """Returns whether a and b are relatively prime to each other."""
    return gcd(a, b) == 1


def both_odd(a, b):
    return a % 2 == 1 and b % 2 == 1


def euclids_formula(m, n, k=1):
    """Returns a pythagorean triple (a, b, c) given values for m, n, and k. If k is omitted, it generates only primitive triples.

    As described in https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    """
    a = k * (m*m - n*n)
    b = k * (2*m*n)
    c = k * (m*m + n*n)

    return (a, b, c)


def gen_pythagorean_triples(maximum_perimiter):
    """Uniquely generates all pythagorean triples up to a given a+b+c.

    It does this by generating values for m, n, and k, and plugs them into euclids_formula,
    starting at each primitive triple (k=1) and generates multiples of that triple up to a
    maximum_perimiter before moving on to the next primitive triples.

    Since there are both infinite primitive triples, and infinite non-primitive triples, generating
    them in order would be unwieldly and I've settled for requiring a maximum_perimiter to be set.

    As described in https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple,
    "where m, n, and k are positive integers with m > n, and with m and n coprime and not both odd"
    """

    for n in count(1):
        for m in count(n+1):
            if coprime(m, n) and not both_odd(m, n):
                primitive_triple = euclids_formula(m, n)

                # If the perimiter of the primitive is over the maximum_perimiter,
                # we will not find another triple with a higher m that is also under
                # the maximum perimeter.
                #
                # If this is the lowest m for a given n, we will ALSO never find any
                # more PRIMITIVE triples under the maximum_perimeter and can quit.
                if sum(primitive_triple) > maximum_perimiter:
                    if m == n+1:
                        return
                    else:
                        break

                yield primitive_triple

                for k in count(2):
                    triple = euclids_formula(m, n, k)

                    # If the perimiter of the multiplied triple is over the maximum_perimiter, we move on to the next primitive.
                    if sum(triple) > maximum_perimiter:
                        break

                    yield triple


def solve(limit=120):
    triangles = defaultdict(set)

    for triple in gen_pythagorean_triples(limit):
        perimeter = sum(triple)
        triangles[perimeter].add(triple)

    single_right_angle_triangles = list(filter(
        lambda k: len(triangles[k]) == 1, triangles))

    return len(single_right_angle_triangles)


if __name__ == "__main__":
    print(solve(1_500_000))
