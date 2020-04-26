"""
Observations:

- In the example 3-gon ring, there are only 2 ways to permutate the inner ring.
- In the 5-gon ring, the inner ring can be permutated in more ways, but **less** than all permutations are needed
  to provide all unique solutions since rotations of the same permutation do not need to be duplicated.
- In the 5-gon ring, it matters that the 10 is in the outside ring - this way it will only give 16 digit answers
"""

from itertools import combinations, permutations
from common.digits import join_digits
from common.logging import info, debug


def rotate(iterable):
    """Rotates the collection one step to the right.

    >>> rotate((1, 2, 3))
    (3, 1, 2)
    """
    return (iterable[-1],) + iterable[:-1]


def rotated_permutations(iterable):
    """Returns the subset of permutations which does not include rotations of the same order of items.

    >>> rotated_permutations((1, 2, 3))
    {(1, 3, 2), (1, 2, 3)}

    >>> rotated_permutations((1, 2, 3, 4))
    {(1, 3, 2, 4), (1, 2, 3, 4), (1, 3, 4, 2), (1, 4, 3, 2), (1, 2, 4, 3), (1, 4, 2, 3)}
    """

    result = set()
    first, *rest = iterable

    # Interestingly, the set of permutations excluding rotations is equal to the set of
    # one of the items concatenated with all permutations of the rest of the items.
    #
    # This is much more efficient than rotating all the permutations to sort them and
    # filter out duplicates, which provides a naive solution to this and lead me to
    # the test case above.
    for permutation in permutations(rest):
        result.add((first,) + permutation)

    return result


def form_inner_ring(numbers):
    """Given the numbers of the internal ring, returns the groups of 2 internal nodes that form the ring.

    >>> form_inner_ring((1, 2, 3))
    ((1, 2), (2, 3), (3, 1))

    >>> form_inner_ring((1, 2, 3, 4, 5))
    ((1, 2), (2, 3), (3, 4), (4, 5), (5, 1))
    """
    groups = []

    for i in range(len(numbers) - 1):
        groups.append(numbers[i:i+2])

    # Close the circle
    groups.append((numbers[-1], numbers[0]))

    return tuple(groups)


def xgon_rings(external_nodes, internal_nodes):
    """Return all valid magic x-gon rings with the given internal and external nodes."""
    rings = []

    for outer_ring in permutations(external_nodes):
        for inner_nodes in rotated_permutations(internal_nodes):
            inner_ring = form_inner_ring(inner_nodes)

            solution = solution_set(outer_ring, inner_ring)
            if solution:
                rings.append(solution)

    return rings


def solution_set(outer_ring, inner_ring):
    """Returns the ordered solution set of a magic x-gon ring if one can be formed, otherwise None."""
    groups = tuple(map(
        lambda r: (r[0],) + r[1],
        zip(outer_ring, inner_ring)))

    # Check that all sums are equal
    totals = set(map(sum, groups))
    if len(totals) != 1:
        return None

    # Orient the ring to start from the group with the numerically lowest external node
    while groups[0][0] != min(outer_ring):
        groups = rotate(groups)

    pretty_info(groups)
    return groups


def pretty_info(ring):
    """Log the ring like in the problem description."""
    total = sum(ring[0])
    solution_set = '; '.join(map(lambda g: ','.join(map(str, g)), ring))

    info(f"{total}\t{solution_set}")


def solve(up_to=6, gons=3):
    numbers = set(range(1, up_to + 1))
    maximum = 0

    for internal_nodes in combinations(numbers, gons):
        # Skip 17-digit solutions
        if 10 in internal_nodes:
            continue

        external_nodes = tuple(numbers - set(internal_nodes))

        for ring in xgon_rings(external_nodes, internal_nodes):
            concatenated = join_digits(map(join_digits, ring))
            maximum = max(maximum, concatenated)

    return maximum


if __name__ == "__main__":
    print(solve(10, 5))
