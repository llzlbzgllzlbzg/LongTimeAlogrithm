from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, num)
        for _ in range(len(nums) - k):
            heapq.heappop(h)
        return heapq.heappop(h)