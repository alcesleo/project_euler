import itertools

# http://www.robertdickau.com/manhattan.html
# https://en.wikipedia.org/wiki/Binomial_coefficient
# https://en.wikipedia.org/wiki/Pascal%27s_triangle

# The number of paths is the central binominal coefficient, which is the middle of row 2n+1 in Pascal's triangle.


def gen_pascal_triangle():
    current_row = [1]

    while True:
        yield current_row

        current_row = [1] + [current_row[i] + current_row[i + 1]
                             for i in range(len(current_row) - 1)] + [1]


LIMIT = 20

row = next(itertools.islice(gen_pascal_triangle(), LIMIT*2, None))
result = row[len(row) // 2]

print(result)
