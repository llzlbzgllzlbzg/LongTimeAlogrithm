# 预处理回文串可以用
# for i in range(n - 1, -1, -1):
#    for j in range(i + 1, n):
#        f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        flag = [[False] * len(s) for _ in range(len(s))] * len(s)
        for start in range(len(s)):
            left, right = start, start
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                flag[left][right] = True
                left -= 1
                right += 1
        for start in range(len(s) - 1):
            left, right = start, start + 1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                flag[left][right] = True
                left -= 1
                right += 1
        result = []
        def backtrack(start: int, path: List[str]):
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start, len(s)):
                if flag[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return result