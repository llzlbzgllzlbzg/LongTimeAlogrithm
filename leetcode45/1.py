from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        max_reach = 0
        next_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                ans += 1
                max_reach = next_reach
            next_reach = max(next_reach, i + num)
        return ans