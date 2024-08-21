#!/usr/bin/python3

"""
https://leetcode.com/problems/walls-and-gates/
https://neetcode.io/problems/islands-and-treasure

You are given a m×n 2D grid initialized with these three possible values:

    -1 - A water cell that can not be traversed. 0 - A treasure chest. INF - A
    land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647
    to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land
cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.
"""

import queue


class Solution:
    def islandsAndTreasure(self, grid) -> None:
        h, w = len(grid), len(grid[0])

        def is_legal(r, c):
            return 0 <= r < h and 0 <= c < w and grid[r][c] != -1

        vis = set()
        q = queue.deque()
        for r in range(0, h):
            for c in range(0, w):
                if grid[r][c] == 0:
                    q.append((r, c))
                    vis.add((r, c))

        dis = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dis
                tmp = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                neighbors = [d for d in tmp if is_legal(*d) and d not in vis]
                for nr, nc in neighbors:
                    q.append((nr, nc))
                    vis.add((nr, nc))
            dis += 1
