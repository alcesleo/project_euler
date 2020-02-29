from common.data import read_data
from problem_018 import parse_triangle, maximum_path

data = read_data("p067_triangle.txt")

triangle = parse_triangle(data)
print(maximum_path(triangle))
