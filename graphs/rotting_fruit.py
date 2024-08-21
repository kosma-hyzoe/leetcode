#!/usr/bin/python3

from queue import deque

"""
https://neetcode.io/problems/rotting-fruit

"""


class Solution:
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        vis = set()

        def is_legal(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS \
                and grid[r][c] not in (0, 2) and (r, c) not in vis

        def get_adj(r, c):
            adjs = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
            return tuple(a for a in adjs if is_legal(*a))

        q = deque()
        n_fruit = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    vis.add((r, c))
                elif grid[r][c] == 1:
                    n_fruit += 1
        if n_fruit == 0:
            return 0

        t = -1
        while q:
            for i in range(len(q)):
                adjs = get_adj(*q.popleft())
                for r, c in adjs:
                    if grid[r][c] == 0:
                        continue

                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        n_fruit -= 1
                    vis.add((r, c))
                    q.append((r, c))
            t += 1
        return t if n_fruit == 0 else -1
