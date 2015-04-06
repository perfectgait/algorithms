#!/usr/bin/env python
"""Report the overall cost of a minimum spanning tree using Prim's minimum spanning tree algorithm"""

__author__ = "Matt Rathbun"
__version__ = "1.0.0"
__license__ = "GPL"


def build_edges(inputs):
    """Build a list of edges from a set of inputs"""
    edges = []

    for line in inputs:
        # @TODO Implement this using a heap
        edges.append([int(field) for field in line.split()])

    return edges


def calculate_cost_of_mst(num_nodes, edges):
    current_node = 1
    X = [current_node]
    T = []
    total_cost = 0

    # Keep going until the MST is connected
    while len(X) < num_nodes:
        cheapest_edge = None

        for edge in edges:
            if ((edge[0] in X and edge[1] not in X) or (edge[1] in X and edge[0] not in X))\
                    and (cheapest_edge is None or edge[2] < cheapest_edge[2]):
                cheapest_edge = edge

        total_cost += cheapest_edge[2]

        if cheapest_edge[0] not in X:
            X.append(cheapest_edge[0])

        if cheapest_edge[1] not in X:
            X.append(cheapest_edge[1])

        T.append(cheapest_edge)

    return total_cost


print "Reading input file..."
inputs = open("edges.txt").read().split("\n")
num_nodes, num_edges = [int(field) for field in inputs[0].split()]
print "Building edges..."
edges = build_edges(inputs[1:])
print "Cost of MST: %d" % calculate_cost_of_mst(num_nodes, edges)