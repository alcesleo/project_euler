"""
In the previous problem I implemented the first pseudocode on Wikipedia,
to improve the performance enough for this problem you simply have to keep
reading and implement the alternative described using a priority queue,
making it fast enough to loop through the paths.

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

from math import inf
from common.data import read_data, parse_grid
from solutions.problem_081 import dijkstra, Vertex, EXAMPLE_DATA


def parse_graph(grid):
    height = len(grid)
    width = len(grid[0])

    graph = {}

    for row in range(height):
        for col in range(width):
            neighbors = []

            if col + 1 < width:
                neighbors.append((row, col + 1))

            if row + 1 < height:
                neighbors.append((row + 1, col))

            if row - 1 >= 0:
                neighbors.append((row - 1, col))

            vertex = Vertex(
                weight=grid[row][col],
                neighbors=neighbors)

            graph[(row, col)] = vertex

    return graph


def solve(data=EXAMPLE_DATA):
    grid = parse_grid(data, separator=",", parse_item=int)
    graph = parse_graph(grid)

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
