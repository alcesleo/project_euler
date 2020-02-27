import os

SCRIPT_PATH = os.path.dirname(__file__)
DATA_PATH = "data/p022_names.txt"
ASCII_OFFSET = offset = ord("A") - 1

with open(os.path.join(SCRIPT_PATH, DATA_PATH), "r") as input_file:
    data = input_file.read()

names = [s.replace('"', "") for s in data.split(",")]
names.sort()


def alphabetical_value(name):
    return sum([ord(c) - ASCII_OFFSET for c in name])


result = sum([alphabetical_value(name) * (position + 1)
              for position, name in enumerate(names)])

print(result)
