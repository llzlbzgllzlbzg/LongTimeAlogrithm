from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def f(index: int, left_num: int, right_num: int, path: str):
            if left_num < right_num or left_num > n or right_num > n:
                return
            elif index == 2 * n:
                self.ans.append(path)
            else:
                f(index + 1, left_num + 1, right_num, path + '(')
                f(index + 1, left_num, right_num + 1, path + ')')
        f(0, 0, 0, '')
        return self.ans