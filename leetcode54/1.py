from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        for i in range((min(m, n) + 1) // 2):
            for j in range(i, n - i):
                res.append(matrix[i][j])
            for j in range(i + 1, m - i):
                res.append(matrix[j][n - i - 1])
            if m - i - 1 > i:
                for j in range(n - i - 2, i - 1, -1):
                    res.append(matrix[m - i - 1][j])
            if n - i - 1 > i:
                for j in range(m - i - 2, i, -1):
                    res.append(matrix[j][i])
        return res