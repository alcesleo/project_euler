"""
"Counting summations" is a bit of a red herring, as this is about partitioning the number:
https://en.wikipedia.org/wiki/Partition_(number_theory)

Looking at the article for the Partition function, the answer to this question is even given as an example p(100):
https://en.wikipedia.org/wiki/Partition_function_(number_theory)*

I already have a partition function from problem 31 which with some optimizations and refactoring is more than
up to the task of this problem as well.

*The only difference from p(100) and the answer to problem 31 being that _at least 2_ numbers are used, and n itself is not counted.
"""

from common.tools import partitions

print(partitions(100) - 1)
