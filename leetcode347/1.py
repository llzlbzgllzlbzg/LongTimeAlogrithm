from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        h = []
        for num, freq in count.items():
            heapq.heappush(h, (-freq, num))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(h)[1])
        return ans