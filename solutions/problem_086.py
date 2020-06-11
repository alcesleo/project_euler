"""
          l
     +---------+
     |        F|
     |         |w
     |         |
     +---------+  <--- fold
     |         |h
     |         |
+----+---------+----+
|    |S        |    |
|    |         |    |
|    |         |    |
+----+---------+----+
     |         |
     |         |
     +---------+

If you unfold the cuboid to a 2D plane, the straight line path S->F
is the hypotenuse of the right angle triangle formed by l and w+h.

    S->F = sqrt(l^2 + (w+h)^2)

To rephrase the question, we need to find integer solutions to Pythagoras'
theorem, and then "fold" the rectangle (l, w+h) at a 90 degree angle into 2
sides of the cuboid (l, w, h) to form all cuboids that fit within M.

Since we ignore rotations you can get (w+h)/2 cuboids, as long as w+h<=M:

           l=4
           M=4
          +---+
          +---+ <--- folds as (4, 1, 3)
    w+h=4 +---+ <--- folds as (4, 2, 2)
          +---+ x--- folds as (4, 3, 1) and is a rotated duplicate
          |   |
          +---+


w+h can exceed M and still be folded into _some_ cuboids that fit within M:

             l=6
             M=6
          +------+
          |      | x--- folds as (6, 1, 7) and is out of bounds
          +------+ <--- folds as (6, 2, 6)
          +------+ <--- folds as (6, 3, 5)
    w+h=8 +------+ <--- folds as (6, 4, 4)
          |      | x--- folds as (6, 5, 3) and is a rotated duplicate
          |      |
          |      |
          |      |
          +------+

We need to exclude these invalid folds which create cuboids which are too large
in a dimension, there are (w+h)-(M+1) of them.

When w+h exceeds 2M it can no longer be folded into any valid cuboid.
"""

from math import sqrt
from itertools import count
from common.logging import info

def solve(target):
    """
    >>> solve(2000)
    100
    """
    solutions = 0

    # Let the length be the bound M
    for length_m in count():
        for width_height in range(2*length_m):
            path = sqrt(length_m**2 + width_height**2)

            if path.is_integer():
                folds = width_height // 2

                if width_height > length_m:
                    folds -= width_height - (length_m + 1)

                solutions += folds

        if solutions > target:
            info(f"Solutions: {solutions}")
            return length_m


if __name__ == "__main__":
    print(solve(1_000_000))
