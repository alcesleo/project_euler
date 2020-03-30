from common.data import read_data, parse_list


ASCII_OFFSET = ord("A") - 1


def alphabetical_value(name):
    return sum([ord(c) - ASCII_OFFSET for c in name])


def solve():
    data = read_data("p022_names.txt")
    names = parse_list(data, separator=",",
                       parse_item=lambda s: s.replace('"', ""))
    names.sort()

    return sum([alphabetical_value(name) * (position + 1)
                for position, name in enumerate(names)])


if __name__ == "__main__":
    print(solve())
