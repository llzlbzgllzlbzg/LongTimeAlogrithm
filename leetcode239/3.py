# 分块+使用前缀和后缀进行预处理 效率不如单调队列
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        prefix, suffix = [0] * len(nums), [0] * len(nums)
        for i in range(len(nums)):
            if i % k == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = max(prefix[i - 1], nums[i])
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1 or (i + 1) % k == 0:
                suffix[i] = nums[i]
            else:
                suffix[i] = max(suffix[i + 1], nums[i])
        for i in range(len(nums) - k + 1):
            ans.append(max(suffix[i], prefix[i + k - 1]))
        return ans
