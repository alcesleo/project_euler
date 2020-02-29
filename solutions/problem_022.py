from common.data import read_data, parse_words

data = read_data("p022_names.txt")
names = parse_words(data)
names.sort()

ASCII_OFFSET = ord("A") - 1


def alphabetical_value(name):
    return sum([ord(c) - ASCII_OFFSET for c in name])


def solve():
    return sum([alphabetical_value(name) * (position + 1)
                for position, name in enumerate(names)])


if __name__ == "__main__":
    print(solve())
