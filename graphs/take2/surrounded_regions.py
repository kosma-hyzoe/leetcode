# foobar
class Solution:
    land_touches_border = False
    land = []

    def solve(self, board):
        ROWS, COLS = len(board), len(board[0])

        vis = set()

        def in_range(r, c):
            return r >= 0 and r < ROWS and c >= 0 and c < COLS

        def look_for_border(r, c):
            if (r, c) in vis:
                return

            self.land.append((r, c))
            vis.add((r, c))
            nbrs = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
            for nbr in nbrs:
                nr, nc = nbr
                if not in_range(*nbr):
                    self.land_touches_border = True
                elif board[nr][nc] == "O":
                    look_for_border(*nbr)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in vis:
                    look_for_border(r, c)

                    if not self.land_touches_border:
                        for lr, lc in self.land:
                            print(lr, lc)
                            board[lr][lc] = "X"
                    self.land_touches_border = False
                    self.land = []
