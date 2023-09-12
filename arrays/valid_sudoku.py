from collections import namedtuple

P = namedtuple("Point", ['x', 'y'])

BOARD_SIZE = 9
LEGAL_NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
BOX_POINTS = [P(1, 1), P(4, 1), P(7, 1),
              P(1, 4), P(4, 4), P(7, 4),
              P(1, 7), P(4, 7), P(7, 7)]
# boxes = {point: set() for point in BOXES_POINTS}


def is_box_valid(p, board):
    box = set()
    for y in range(p.y - 1, p.y + 2):
        for x in range(p.x - 1, p.x + 2):
            val = board[y][x]
            if val == ".":
                continue
            if val in box:
                return False
            box.add(val)
    return True


class Solution:
    def isValidSudoku(self, board):
        columns = [set() for _ in range(BOARD_SIZE)]
        rows = [set() for _ in range(BOARD_SIZE)]
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if board[y][x] == ".":
                    continue

                num = board[y][x]
                if num in columns[x] or num in rows[y]:
                    return False
                columns[x].add(num)
                rows[y].add(num)

        for p in BOX_POINTS:
            if not is_box_valid(p, board):
                return False
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().isValidSudoku(board)