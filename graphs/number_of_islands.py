from collections import namedtuple

P = namedtuple("Point", ['x', 'y'])

class Solution:
    q = []
    # TODO change to a dict
    visited = []
    @staticmethod
    def inBounds(p, w, h):
        return 0 <= p.x < w and 0 <= p.y < h

    def checkNeigbors(self, p, grid):
        nbrs = [P(p.x - 1, p.y), P(p.x + 1, p.y), P(p.x, p.y - 1), P(p.x, p.y + 1)]
        for n in nbrs:
            if not Solution.inBounds(n, len(grid[0]), len(grid)):
                continue
            elif grid[n.y][n.x] == "1" and (n.x, n.y) not in self.visited:
                self.visited.append(P(n.x, n.y))
                self.q.append(P(n.x, n.y))

    def numIslands(self, grid):
        n_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and (x, y) not in self.visited:
                    n_islands += 1
                    self.visited.append(P(x, y))
                    self.q.append(P(x, y))
                    while self.q:
                        self.checkNeigbors(self.q.pop(0), grid)
        return n_islands


print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))