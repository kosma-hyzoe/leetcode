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


class Solution:
    def islandsAndTreasure(self, grid) -> None:
        h, w = len(grid), len(grid[0])
        INF = 2147483647

        def is_legal(r, c):
            return 0 <= r < h and 0 <= c < w and grid[r][c] != -1

        def helper(r, c):
            dis = 0
            best = INF
            vis = set()

            q = [(r, c)]
            while q:
                cr, cc = q.pop(0)
                tmp = [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]
                neighbors = [d for d in tmp if is_legal(*d) and d not in vis]
                dis += 1
                for nr, nc in neighbors:
                    if grid[nr][nc] == 0:
                        if dis < best:
                            best = dis
                    elif grid[nr][nc] != INF:
                        if dis + grid[nr][nc] < best:
                            best = dis + grid[nr][nc]
                    q.append((nr, nc))
                    vis.add((nr, nc))
            grid[r][c] = best

        for r in range(0, h):
            for c in range(0, w):
                if grid[r][c] == INF:
                    helper(r, c)
