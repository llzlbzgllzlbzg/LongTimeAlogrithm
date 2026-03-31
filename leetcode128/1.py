from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        ans = 1
        hashtable = set(nums)
        flag = dict.fromkeys(nums, 0)
        for i in range(len(nums)):
            if flag[nums[i]] > 0:
                continue
            count = 0
            current_num = nums[i]
            while current_num + 1 in hashtable:
                count += 1
                current_num += 1
                if flag[current_num] > 0:
                    break
                flag[current_num] = 1
            flag[nums[i]] = flag[current_num] + count
            if flag[current_num] == 0:
                flag[nums[i]] += 1
            if flag[nums[i]] > ans:
                ans = flag[nums[i]]
        return ans