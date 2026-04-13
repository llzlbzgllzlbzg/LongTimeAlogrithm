from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ans = []
        dict_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        s = list(digits)
        def f(index: int, record: List[str]) -> None:
            if index == len(digits):
                self.ans.append(''.join(record))
            else:
                for ch in dict_map[digits[index]]:
                    record.append(ch)
                    f(index + 1, record)
                    record.pop()
        f(0, [])
        return self.ans