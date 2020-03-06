from itertools import count
from common.tools import digits

for i in count(1):
    if set(digits(i)) == \
            set(digits(i * 2)) == \
            set(digits(i * 3)) == \
            set(digits(i * 4)) == \
            set(digits(i * 5)) == \
            set(digits(i * 6)):

        print(i)
        break
