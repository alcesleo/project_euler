"""
In the previous problem I implemented the first pseudocode on Wikipedia,
to improve the performance enough for this problem you simply have to keep
reading and implement the alternative described using a priority queue,
making it fast enough to loop through the paths.

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

from math import inf
from common.data import read_data, parse_grid
from solutions.problem_081 import parse_graph, dijkstra, EXAMPLE_DATA


def solve(data=EXAMPLE_DATA):
    grid = parse_grid(data, separator=",", parse_item=int)
    graph = parse_graph(grid, directions=[(0, 1), (1, 0), (-1, 0)])

    height = len(grid)
    width = len(grid[0])

    result = inf

    for start_row in range(height):
        dist, prev = dijkstra(graph, (start_row, 0))

        for end_row in range(height):
            distance = grid[start_row][0] + dist[(end_row, width - 1)]

            if distance < result:
                result = distance

    return result


if __name__ == "__main__":
    data = read_data("p082_matrix.txt")
    print(solve(data))
