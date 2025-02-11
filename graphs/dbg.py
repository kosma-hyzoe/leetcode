#!/usr/bin/python3

from graph_valid_tree import Solution

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(Solution().validTree(n, edges))
