"""
I started out solving this problem by implementing the principle in the link from the Math Stack Exchange,
and spent a lot of time messing with the precision of the Decimal class before it becoming painfully
obvious that it was never going to be fast or reliable when using floats.

I also spent some time making a way to detect when the period repeats, which involved checking a threshold
of repetitions as already at sqrt(13) the period repeats the 1 4 times before it gets a different digit
and starts repeating. So at this point I had like 3 different limits and thresholds that I was just experimenting
with to get it to run fast enough without simply producing incorrect results as the decimal precision runs out.

If I cranked all the limits up to 11 and let it run overnigh, I think it would have gotten the right answer in the
end, but it was just not a great solution. In the end I simply ported the C++ code from the accepted answer on
this Stack Overflow question, which magically works, is really fast, and even finds the repeating period right away
without even checking for it. I cannot claim to fully understand how.

https://en.wikipedia.org/wiki/Continued_fraction
https://math.stackexchange.com/questions/265690/continued-fraction-of-a-square-root
https://stackoverflow.com/questions/12182701/generating-continued-fractions-for-square-roots
"""

from math import sqrt
from common.continued_fractions import period_of_root
from common.logging import logger


def solve(limit=13):
    odd_periods = 0

    for n in range(2, limit + 1):
        a0, *period = period_of_root(n)

        if len(period) % 2 != 0:
            odd_periods += 1

        if period:
            logger.info(
                f"√{n} = [{a0}; {tuple(period)}], period={len(period)}")
        else:
            logger.debug(f"√{n} = {sqrt(n)}")

    return odd_periods


if __name__ == "__main__":
    print(solve(10_000))
