#!/usr/bin/python3

"""
https://leetcode.com/problems/walls-and-gates/
https://neetcode.io/problems/islands-and-treasure
"""


class Solution:
    def islandsAndTreasure(self, grid) -> None:
        h, w = len(grid), len(grid[0])
        INF = 2147483647

        def is_legal(r, c):
            return 0 <= r < h and 0 <= c < w and grid[r][c] != -1

        def helper(r, c):
            q = [(r, c)]
            while q:
                cr, cc = q.pop(0)
                tmp = [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]
                neighbors = [d for d in tmp if is_legal(*d)]
                for nr, nc in neighbors:
                    if grid[nr][nc] == 0:
                        grid[cr][cc] = 1
                    elif grid[nr][nc] != INF:
                        grid[cr][cc] = grid[nr][nc] + 1
                    else:
                        q.append((nr, nc))

        for r in range(0, h):
            for c in range(0, w):
                if grid[r][c] == INF:
                    helper(r, c)
