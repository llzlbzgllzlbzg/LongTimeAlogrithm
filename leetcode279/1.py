class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        num = 1
        dp = [0] * n
        while num * num <= n:
            squares.append(num * num)
            dp[num * num - 1] = 1
            num += 1
        for i in range(n):
            if dp[i] == 1:
                continue
            min_dp_i_j = i
            for j in squares:
                if i - j < 0:
                    break
                else:
                    min_dp_i_j = min(min_dp_i_j, dp[i - j])
            dp[i] = min_dp_i_j + 1
        return dp[n - 1]