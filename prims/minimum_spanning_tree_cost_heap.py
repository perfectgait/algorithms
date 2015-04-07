#!/usr/bin/env python
"""Report the overall cost of a minimum spanning tree using Prim's minimum spanning tree algorithm with a heap"""

from heapq import heappush, heappop

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def build_edges(inputs):
    """Build a heap of edges from a set of inputs"""
    edges = []

    for line in inputs:
        fields = line.split()
        heappush(edges, (int(fields[2]), [int(field) for field in fields]))

    return edges


def calculate_cost_of_mst(num_nodes, edges):
    X = [1]
    T = []
    total_cost = 0

    edges.sort()

    while len(X) < num_nodes:
        for i in range(len(edges)):
            cost, cheapest_edge = edges[i]

            if (cheapest_edge[0] in X and cheapest_edge[1] not in X)\
                    or (cheapest_edge[0] not in X and cheapest_edge[1] in X):
                total_cost += cost

                if cheapest_edge[0] not in X:
                    X.append(cheapest_edge[0])

                if cheapest_edge[1] not in X:
                    X.append(cheapest_edge[1])

                T.append(cheapest_edge)

                break

    return total_cost


print "Reading input file..."
inputs = open("edges.txt").read().split("\n")
num_nodes, num_edges = [int(field) for field in inputs[0].split()]
print "Building edges..."
edges = build_edges(inputs[1:])
print "Cost of MST: %d" % calculate_cost_of_mst(num_nodes, edges)