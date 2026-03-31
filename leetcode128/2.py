from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        hashtable = set(nums)
        for num in hashtable:
            if num - 1 not in hashtable:
                current_num = num
                count = 1
                while current_num + 1 in hashtable:
                    current_num += 1
                    count += 1
                ans = max(ans, count)
        return ans