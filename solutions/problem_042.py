import itertools
from common.data import read_strs
from problem_022 import alphabetical_value
from problem_012 import gen_triangle_numbers

words = read_strs("p042_words.txt")

limit = 10_000
triangle_numbers = set(itertools.islice(gen_triangle_numbers(), limit))

count = 0
for word in words:
    if alphabetical_value(word) in triangle_numbers:
        count += 1

print(count)
