import os
from problem_18 import parse_triangle, maximum_path

SCRIPT_PATH = os.path.dirname(__file__)
DATA_PATH = "data/p067_triangle.txt"

with open(os.path.join(SCRIPT_PATH, DATA_PATH), "r") as input_file:
    data = input_file.read()


TRIANGLE = parse_triangle(data)
print(maximum_path(TRIANGLE))
