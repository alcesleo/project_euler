from math import log
from common.data import read_data

data = read_data("p099_base_exp.txt")

highest = 0
highest_line = 0

for line_number, base_exp in enumerate(data.splitlines(), 1):
    base, exp = map(int, base_exp.split(","))

    # https://www.rapidtables.com/math/algebra/logarithm/Logarithm_Rules.html#power%20rule
    number = log(base) * exp

    if number > highest:
        highest = number
        highest_line = line_number

print(highest_line)
