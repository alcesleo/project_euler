"""Read and parse text files from the data/ directory"""

import os

SCRIPT_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(SCRIPT_PATH, "../data/")


def read_data(filename):
    """Read a text file from the data/ directory
    """
    with open(os.path.join(DATA_PATH, filename), "r") as data_file:
        return data_file.read()


def parse_list(data, separator=" ", parse_item=str):
    """Parses text into a list.

    >>> parse_list("01,02,03,04", separator=",", parse_item=int)
    [1, 2, 3, 4]
    """
    return list(map(parse_item, data.split(separator)))


def parse_grid(data, separator=" ", parse_item=str):
    """Parses multiline text into a 2d array.

    >>> parse_grid("\\n01,02\\n03,04\\n", separator=",", parse_item=int)
    [[1, 2], [3, 4]]
    """
    grid = []

    for row in data.strip().splitlines():
        grid.append(parse_list(row, separator, parse_item))

    return grid
