from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0] * i for i in range(1, numRows + 1)]
        ans[0][0] = 1
        for row in range(1, numRows):
            for col in range(row + 1):
                if col == 0 or col == row:
                    ans[row][col] = 1
                else:
                    ans[row][col] = ans[row - 1][col - 1] + ans[row - 1][col]
        return ans