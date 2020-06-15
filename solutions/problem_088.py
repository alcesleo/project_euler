"""
* The 1s don't matter for the product, only for the sum.
* The minimum is always >k since the minimum possible sum would have k 1s.
* The minimum is always <=2k since we can always use {2, k} and
  pad with ones to get a product-sum equal to 2k, e.g:

    * 1+1+2+4=8, 1*1*2*4=8
    * 1+1+1+1+2+6=12, 1*1*1*1*2*6=12

I've designed the algorithm as a Breadth First Search through
a binary tree that looks as the example below, padded 1:s have
been added for clarity:

              k=4    1112
            __________/\__________
           /                      \
         1122                    1113
      ____/\____              ____/\____
     /          \            /          \
   1222        1123        1133        1114
   _/\_        _/\_        _/\_        _/\_
  /    \      /    \      /    \      /    \
2222  1223  1233  1124  1333  1134  1144  1115

* each right child increments the rightmost number
* each left child pushes another number in from the right

This will try combinations with many low numbers, or few big
numbers first, which is the pattern these seem to take (e.g.
a bunch of 2's or a large number at the end.

I tried really hard to make this a binary search which would
be a lot faster, but couldn't find a way to determine which
side of the tree must contain the minimum solution (or a tree
structure where that question can be answered).

This solution is a lot quicker than some other solutions I tried
but still nowhere near fast enough at over 10m.
"""

from math import prod, inf
from collections import deque

from common.logging import info, debug, warning


def minimal_product_sum(k):
    """
    >>> minimal_product_sum(5)
    8

    >>> minimal_product_sum(6)
    12
    """

    queue = deque([(2,)])
    minimum = inf
    k2 = k * 2

    while queue:
        a = queue.popleft()
        kl = len(a) # k discounting the 1's

        p = prod(a)
        s = sum(a) + (k - kl) # Pad with 1's

        # Both padding and increasing yields larger numbers,
        # if p or s is already above k2, their children also
        # will be, and we know that the minimum is below k2.
        if p > k2 or s > k2:
            continue

        if p == s and p < minimum:
            info(f"k={k}: {s} = {a}")
            minimum = p

        if kl < k:
            left = a + (a[-1],)
            queue.append(left)

        if a[-1] < k:
            right = a[:-1] + (a[-1] + 1,)
            queue.append(right)

    return minimum


def solve(limit):
    """
    >>> solve(6)
    30

    >>> solve(12)
    61
    """
    product_sums = set()

    for k in range(2, limit + 1):
        product_sums.add(minimal_product_sum(k))

    info(product_sums)

    return sum(product_sums)


if __name__ == "__main__":
    print(solve(12_000))
