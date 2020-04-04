"""
At this point, even though the difficulty is 15%(!) higher than 81, it's exactly
the same problem but with more neighbors added when parsing the graph. Worth noting
is that it's now a cyclic graph, which could have been a problem but as we are already
using keys in a dict to distinguish the nodes, and the Dijkstra algorithm being designed
for this use case as well, it poses no issues and even runs a lot faster than 82 since we
don't have to loop through the different possible rows and only need to find one path.
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

            if col - 1 >= 0:
                neighbors.append((row, col - 1))

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

    top_left = (0, 0)
    bottom_right = (len(grid) - 1, len(grid[0]) - 1)

    dist, prev = dijkstra(graph, top_left)
    return(grid[0][0] + dist[bottom_right])


if __name__ == "__main__":
    data = read_data("p083_matrix.txt")
    print(solve(data))
