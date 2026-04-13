from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def f(index: int, cur: List[int]) -> None:
            if index == len(nums):
                self.ans.append(cur.copy())
            else:
                for i in range(index, len(nums)):
                    nums[index], nums[i] = nums[i], nums[index]
                    cur.append(nums[index])
                    f(index + 1, cur)
                    cur.pop()
                    nums[index], nums[i] = nums[i], nums[index]
        f(0, [])
        return self.ans