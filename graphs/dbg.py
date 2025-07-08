#!/usr/bin/python3

from graph_valid_tree import Solution

print("---")
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
assert Solution().validTree(n, edges) is True

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(Solution().validTree(n, edges))
n = 4
edges = [[0, 1], [2, 3]]
print(Solution().validTree(n, edges))
