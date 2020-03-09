from itertools import count
from common.tools import split_digits

for i in count(1):
    if set(split_digits(i)) == \
            set(split_digits(i * 2)) == \
            set(split_digits(i * 3)) == \
            set(split_digits(i * 4)) == \
            set(split_digits(i * 5)) == \
            set(split_digits(i * 6)):

        print(i)
        break
