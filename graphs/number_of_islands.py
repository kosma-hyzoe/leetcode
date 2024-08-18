import queue


class Solution:
    def numIslands(self, grid):
        count = 0
        visited = set()
        h, w = len(grid), len(grid[0])

        def bfs(r, c):
            q = queue.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                ro, co = q.popleft()
                d = [(ro - 1, co), (ro + 1, co), (ro, co - 1), (ro, co + 1)]
                for n in d:
                    if h > n[0] >= 0 and w > n[1] >= 0  \
                        and grid[n[0]][n[1]] == "1" and \
                            (n[0], n[1]) not in visited:
                        q.append(n)
                        visited.add(n)

        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    count += 1
                    bfs(r, c)
        return count
