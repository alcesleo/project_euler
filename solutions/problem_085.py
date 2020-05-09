"""
I started by listing the number of rectangles by grid size:

    1   2   3   4
   ________________
1 | 1   3   6   10
2 | 3   9   18  30
3 | 6   18  36  60
4 | 10  30  60  100

When I first did this on paper, I actually got several of them wrong, but
drawing a grid like this made them stand out and I could go back and
correct them, seeing that this pattern actually holds.

While correcting my errors, I found that a reliable way of counting the
number of rectangles by hand was to let each square in the grid represent
a size of a rectangle, the top left representing a 1x1 square and the bottom
right representing the entire grid filled in.

A pattern of how many rectangles of each shape emerges:

   ____ ____ ____
  | 12 |  8 |  4 |
  |  9 |  6 |  3 |
  |  6 |  4 |  2 |
  |  3 |  2 |  1 |
   ____ ____ ____

Counting each square by this method however is not needed as it can be seen from the
first grid that the number of rectangles in each grid size is the product of the
triangle numbers T(width) * T(height).

This lets us rephrase the question:

What's the product of width * height where T(width) * T(height) most closely equals 2,000,000?
"""

from math import inf
from common.polygonal import triangle
from common.logging import info


def solve(target=91, limit=6):
    result_area, result_delta = 0, inf

    for h in range(1, limit):
        for w in range(1, limit):
            rectangles = triangle(h) * triangle(w)
            delta = abs(rectangles - target)
            area = h * w

            if delta < result_delta:
                result_area, result_delta = area, delta
                info(f"{h}x{w}: rectangles={rectangles}, delta={delta}, area={area}")

    return result_area


if __name__ == "__main__":
    print(solve(2_000_000, 100))
