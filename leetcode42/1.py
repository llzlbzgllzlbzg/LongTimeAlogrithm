from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_height, right_height = height[left], height[right]
        ans = 0
        while left < right:
            if left_height < right_height:
                left += 1
                left_height = max(left_height, height[left])
                ans += left_height - height[left]
            else:
                right -= 1
                right_height = max(right_height, height[right])
                ans += right_height - height[right]
        return ans