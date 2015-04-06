# [Prim's minimum spanning tree algorithm](http://en.wikipedia.org/wiki/Prim%27s_algorithm)

## Problems
### Question 1
This file describes an undirected graph with integer edge costs. It has the format

number_of_nodes number_of_edges

one_node_of_edge_1 other_node_of_edge_1 edge_1_cost

one_node_of_edge_2 other_node_of_edge_2 edge_2_cost

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and
vertex #3 that has cost -8874. You should NOT assume that edge costs are positive, nor should you assume that they are
distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a
minimum spanning tree.