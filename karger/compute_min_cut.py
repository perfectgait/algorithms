#!/usr/bin/env python
"""This will compute the minimum cut from an input using Karger's randomized contraction algorithm."""

import random, copy

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def find_minimum_cut(graph):
    """Find the minimum cut of a graph using Karger's randomized contradiction algorithm"""
    while len(graph) > 2:
        u, v = choose_random_edge(graph)
        merge_edge(graph, u, v)

        # Remove self-loops
        while u in graph[u]:
            graph[u].remove(u)

        # Remove vertex from graph
        del graph[v]

    # The length of the first remaining vertex is the size of the minimum cut
    return len(graph[graph.keys()[0]])


def choose_random_edge(graph):
    """Choose a random edge (u, v) from a graph"""
    keys = graph.keys()
    u = keys[random.randint(0, len(keys) - 1)]
    v = graph[u][random.randint(0, len(graph[u]) - 1)]

    return u, v


def merge_edge(graph, u, v):
    """Merge an edge into a single vertex"""
    # Attach v's adjacency list to u's adjacency list
    graph[u].extend(graph[v])

    # Go through all of the vertices in v's adjacency list and replace all instances of v in those adjacency lists with
    # u
    for i in graph[v]:
        adjacency_list = graph[i]

        for j in range(0, len(adjacency_list)):
            if adjacency_list[j] == v:
                adjacency_list[j] = u


graph = {}
lines = [line.strip().rstrip('\r\n').split('\t') for line in open('kargerMinCut.txt')]

for line in lines:
    graph[int(line[0])] = [int(i) for i in line[1:]]

minimum_cut = find_minimum_cut(copy.deepcopy(graph))

for i in range(0, 100):
    next_minimum_cut = find_minimum_cut(copy.deepcopy(graph))

    if next_minimum_cut < minimum_cut:
        minimum_cut = next_minimum_cut

print "Minimum Cut: %d" % minimum_cut