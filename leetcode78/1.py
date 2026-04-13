from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def f(index: int, path: List[int]) -> None:
            print('f', index, path)
            if index == len(nums):
                self.ans.append(path.copy())
            else:
                f(index + 1, path)
                path.append(nums[index])
                f(index + 1, path)
                path.pop()
        f(0, [])
        return self.ans