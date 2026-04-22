from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp1, dp2 = [], []
        for i in range(n):
            dp1.append(nums[i])
            dp2.append(nums[i])
        for i in range(1, n):
                dp1[i] = max(dp1[i - 1] * nums[i], nums[i], dp2[i - 1] * nums[i])
                dp2[i] = min(dp2[i - 1] * nums[i], nums[i], dp1[i - 1] * nums[i])
        return max(dp1)