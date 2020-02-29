from common.data import read_data

data = read_data("p022_names.txt")
names = [s.replace('"', "") for s in data.split(",")]
names.sort()

ASCII_OFFSET = offset = ord("A") - 1


def alphabetical_value(name):
    return sum([ord(c) - ASCII_OFFSET for c in name])


result = sum([alphabetical_value(name) * (position + 1)
              for position, name in enumerate(names)])

print(result)
