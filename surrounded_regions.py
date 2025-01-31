# https://neetcode.io/problems/surrounded-regions

import queue


class Solution:
    def solve(self, board):
        vis = set()

        ROWS, COLS = len(board), len(board[0])

        def is_leg(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def helper(el):
            group = set([el])
            to_cross = True

            q = queue.Queue()
            q.put(el)
            while not q.empty():
                r, c = q.get()
                nbrs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in nbrs:
                    if not is_leg(nr, nc):
                        to_cross = False
                        continue
                    if (nr, nc) in vis:
                        continue

                    if board[nr][nc] == 'O':
                        vis.add((nr, nc))
                        group.add((nr, nc))
                        q.put((nr, nc))

            if to_cross:
                for r, c in group:
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in vis:
                    vis.add((r, c))
                    helper((r, c))


b = [["X","O","X","O","X","O","O","O","X","O"],["X","O","O","X","X","X","O","O","O","X"],["O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","X","O","O","X"],["O","O","X","X","O","X","X","O","O","O"],["X","O","O","X","X","X","O","X","X","O"],["X","O","X","O","O","X","X","O","X","O"],["X","X","O","X","X","O","X","O","O","X"],["O","O","O","O","X","O","X","O","X","O"],["X","X","O","X","X","X","X","O","O","O"]]
for r in b:
    print(r)
print("---")
Solution().solve(b)
for r in b:
    print(r)
