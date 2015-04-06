#!/usr/bin/env python
"""This will compute the shortest paths of a graph using Dijkstra's shortest-path algorithm."""

import sys

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def build_graph(data):
    """Build a graph where each line in data contains a vertex as the first element and pairs of tuples thereafter"""
    graph = {}

    for line in data:
        fields = line.split()
        vertex = int(fields[0])
        edges = [tuple([int(i) for i in f.split(",")]) for f in fields[1:]]
        graph[vertex] = edges

    return graph


def shortest_path(graph, start):
    """Compute all shortest paths for a graph from a starting vertex using Dijkstra's shortest-path algorithm"""

    X = {start: True}
    A = {start: 0}

    while len(X) != len(graph):
        processed_vertex = None
        minimum_distance = sys.maxint

        for current_vertex in X:
            for vertex, distance in graph[current_vertex]:
                if vertex not in X:
                    # @TODO Use heap
                    if A[current_vertex] + distance < minimum_distance:
                        processed_vertex = vertex
                        minimum_distance = A[current_vertex] + distance

        X[processed_vertex] = True
        A[processed_vertex] = minimum_distance

    return A


data = open("dijkstraData.txt").read().split("\n")
graph = build_graph(data)
shortest_paths = shortest_path(graph, 1)
# shortest_path_vertexes = [10, 30, 50, 80, 90, 110, 130, 160, 180, 190]
shortest_path_vertexes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

print [shortest_paths[vertex] for vertex in shortest_path_vertexes]