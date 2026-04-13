from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def f(index: int, numSum: int, path: List[int]) -> None:
            if index == len(candidates):
                return
            while numSum < target:
                f(index + 1, numSum, path.copy())
                path.append(candidates[index])
                numSum += candidates[index]
            if numSum == target:
                self.ans.append(path.copy())
        f(0, 0, [])
        return self.ans