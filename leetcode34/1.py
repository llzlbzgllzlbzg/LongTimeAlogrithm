from typing import List
import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        for right in range(left, len(nums)):
            if nums[right] != nums[left]:
                return [left, right - 1]
        return [left, len(nums)]