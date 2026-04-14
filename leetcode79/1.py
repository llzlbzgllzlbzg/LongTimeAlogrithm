from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        rows = len(board)
        cols = len(board[0])
        flag = [[False] * cols for _ in range(rows)]

        def dfs(i, j, index):
            if index == len(word):
                return True
            
            if i - 1 >= 0 and not flag[i - 1][j] and board[i - 1][j] == word[index]:
                flag[i - 1][j] = True
                if dfs(i - 1, j, index + 1):
                    return True
                flag[i - 1][j] = False

            if i + 1 < rows and not flag[i + 1][j] and board[i + 1][j] == word[index]:
                flag[i + 1][j] = True
                if dfs(i + 1, j, index + 1):
                    return True
                flag[i + 1][j] = False

            if j - 1 >= 0 and not flag[i][j - 1] and board[i][j - 1] == word[index]:
                flag[i][j - 1] = True
                if dfs(i, j - 1, index + 1):
                    return True
                flag[i][j - 1] = False

            if j + 1 < cols and not flag[i][j + 1] and board[i][j + 1] == word[index]:
                flag[i + 1][j] = True
                if dfs(i, j + 1, index + 1):
                    return True
                flag[i][j + 1] = False

            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    flag[i][j] = True
                    if dfs(i, j, 1):
                        return True
                    flag[i][j] = False
        return False