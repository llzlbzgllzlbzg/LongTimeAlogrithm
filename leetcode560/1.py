from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        suffix = 0
        ans = 0
        hashmap = dict()
        hashmap[0] = 1
        for i in range(len(nums)):
            suffix += nums[i]
            if suffix - k in hashmap:
                ans += hashmap[suffix - k]
            hashmap[suffix] = hashmap.get(suffix, 0) + 1
        return ans