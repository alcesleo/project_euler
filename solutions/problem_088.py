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

Every product will have a matching sum that you get by padding the product with
1's, giving a solution for a value of k.

Going through this tree up to 2k and keeping track of the minimum
for each k yields the solution.
"""

from math import prod, inf
from collections import deque, defaultdict

from common.logging import info


def solve(limit):
    """
    >>> solve(6)
    30

    >>> solve(12)
    61
    """

    minimum = defaultdict(lambda: inf)
    queue = deque([(2,)])
    k2 = limit * 2

    while queue:
        numbers = queue.popleft()

        p = prod(numbers)
        s = sum(numbers)
        k = len(numbers) + (p - s)

        if p > k2:
            continue

        if k > 1 and k <= limit:
            minimum[k] = min(minimum[k], p)

        info(f"k={k}: {s} = {numbers}")

        left = numbers + (numbers[-1],)
        queue.append(left)

        right = numbers[:-1] + (numbers[-1] + 1,)
        queue.append(right)

    product_sums = set(minimum.values())
    info(product_sums)

    return sum(product_sums)


if __name__ == "__main__":
    print(solve(12_000))
