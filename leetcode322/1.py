from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min_dp_i_j = -1
            for j in coins:
                if i - j < 0 or dp[i - j] == -1:
                    continue
                min_dp_i_j = min(min_dp_i_j, dp[i - j]) if min_dp_i_j != -1 else dp[i - j]
            if min_dp_i_j != -1:
                dp[i] = min_dp_i_j + 1
        return dp[amount]