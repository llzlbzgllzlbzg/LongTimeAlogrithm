class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        max_left = 0
        max_right = 0
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, n):
                if j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = ((s[i] == s[j]) and dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_left = i
                    max_right = j
        return s[max_left:(max_right + 1)]