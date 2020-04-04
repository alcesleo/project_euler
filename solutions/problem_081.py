"""
The grid represents a weighted directed graph, all we need to do
is parse it as such and use Dijkstra's algorithm to find the path.

I've implemented it before:

https://github.com/alcesleo/go-playground/blob/d6f9932b65f34d38556fe5170bc7dad46277a7a6/dijkstra/dijkstra.go

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
https://www.python.org/doc/essays/graphs/
"""

from math import inf
from collections import namedtuple
from queue import PriorityQueue
from common.data import read_data, parse_grid
from common.logging import logger


EXAMPLE_DATA = """
    131,673,234,103,18
    201,96,342,965,150
    630,803,746,422,111
    537,699,497,121,956
    805,732,524,37,331
"""


Vertex = namedtuple("Vertex", ["weight", "neighbors"])


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

            vertex = Vertex(
                weight=grid[row][col],
                neighbors=neighbors)

            graph[(row, col)] = vertex

    return graph


def dijkstra(graph, start):
    queue = PriorityQueue()
    queue.put((0, start))

    distance = {}
    previous = {}

    for vertex in graph:
        distance[vertex] = inf
        previous[vertex] = None

    distance[start] = 0

    while not queue.empty():
        _, vertex = queue.get()

        weight, neighbors = graph[vertex]

        for neighbor in neighbors:
            alt = distance[vertex] + graph[neighbor].weight

            if alt < distance[neighbor]:
                distance[neighbor] = alt
                previous[neighbor] = vertex

                queue.put((distance[neighbor], neighbor))

    return distance, previous


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
    data = read_data("p081_matrix.txt")
    print(solve(data))