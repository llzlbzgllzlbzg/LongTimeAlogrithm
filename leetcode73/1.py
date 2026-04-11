from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_hash = set()
        col_hash = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_hash.add(i)
                    col_hash.add(j)
        for i in row_hash:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in col_hash:
            for i in range(len(matrix)):
                matrix[i][j] = 0