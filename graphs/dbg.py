#!/usr/bin/python3

from graph_valid_tree import Solution
print(">>>")

print("---")
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
<<<<<<< HEAD
assert Solution().validTree(n, edges) is True

=======
print(Solution().validTree(n, edges) is False)
print("---")
>>>>>>> 0dd4e73b320806c370e4d17f6dfdb077c37ea6b3
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(Solution().validTree(n, edges) is True)
print("---")
n = 4
edges = [[0, 1], [2, 3]]
print(Solution().validTree(n, edges))
