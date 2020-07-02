import itertools
from common.data import read_data, parse_list
from solutions.problem_022 import alphabetical_value
from solutions.problem_012 import gen_triangle_numbers

def solve():
    data = read_data("p042_words.txt")
    words = parse_list(data, separator=",",
                    parse_item=lambda s: s.replace('"', ""))

    limit = 10_000
    triangle_numbers = set(itertools.islice(gen_triangle_numbers(), limit))

    count = 0
    for word in words:
        if alphabetical_value(word) in triangle_numbers:
            count += 1

    return count

if __name__ == "__main__":
    print(solve())
