from  typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = nums[i]
        for i in range(len(nums) - zero_count, len(nums)):
            nums[i] = 0