from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1] * n
        res = []
        rows = ['.'] * n
        def solve(row: int, cols: int, dias1: int, dias2: int):
            if row == n:
                board = []
                for i in range(n):
                    rows[queens[i]] = "Q"
                    board.append("".join(rows))
                    rows[queens[i]] = "."
                res.append(board)
            else:
                available = ((1 << n) - 1) & (~(cols | dias1 | dias2))
                while available:
                    pos = available & (-available)
                    available = available & (available - 1)
                    col = bin(pos - 1).count("1")
                queens[row] = col
                solve(row + 1, cols | pos, (dias1 | pos) << 1, (dias2 | pos) >> 1)

        solve(0, 0, 0, 0)
        return res