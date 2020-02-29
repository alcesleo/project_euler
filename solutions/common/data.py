import os

SCRIPT_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(SCRIPT_PATH, "../data/")


def read_data(filename):
    """Read a text file from the data/ directory
    """
    with open(os.path.join(DATA_PATH, filename), "r") as data_file:
        return data_file.read()


def parse_words(data):
    return [s.replace('"', "") for s in data.split(",")]
