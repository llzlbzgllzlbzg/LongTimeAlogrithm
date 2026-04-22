from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        for num in nums:
            if num > total // 2:
                return False
        dp = [[False] * (total // 2 + 1) for _ in range(n)]
        dp[0][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            dp[i][0] = True
            for j in range(1, total // 2 + 1):
                dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i]] if j - nums[i] >= 0 else False)
        return dp[n - 1][total // 2]