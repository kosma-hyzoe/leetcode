from collections import namedtuple

P = namedtuple("Point", ['x', 'y'])
BOARD_SIZE = 9


class Solution:
    def isValidSudoku(self, board):
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        columns = [set() for _ in range(BOARD_SIZE)]
        rows = [set() for _ in range(BOARD_SIZE)]
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if board[y][x] == ".":
                    continue

                num = board[y][x]
                box = boxes[y // 3][x // 3]
                if num in box or num in columns[x] or num in rows[y]:
                    return False
                box.add(num)
                columns[x].add(num)
                rows[y].add(num)
        return True


board = [
    [".","8","7","6","5","4","3","2","1"],
    ["2",".",".",".",".",".",".",".","."],
    ["3",".",".",".",".",".",".",".","."],
    ["4",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".",".","."],
    ["6",".",".",".",".",".",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    ["8",".",".",".",".",".",".",".","."],
    ["9",".",".",".",".",".",".",".","."]
]

assert Solution().isValidSudoku(board)
