import itertools
from common.data import read_data, parse_words
from problem_022 import alphabetical_value
from problem_012 import gen_triangle_numbers

data = read_data("p042_words.txt")
words = parse_words(data)

limit = 10_000
triangle_numbers = set(itertools.islice(gen_triangle_numbers(), limit))

count = 0
for word in words:
    if alphabetical_value(word) in triangle_numbers:
        count += 1

print(count)
