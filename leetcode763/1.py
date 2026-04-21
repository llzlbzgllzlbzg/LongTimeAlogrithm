from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_map = {}
        for i, ch in enumerate(s):
            last_map[ch] = i
        ans = []
        start, end = 0, 0
        for i, ch in enumerate(s):
            end = max(end, last_map[ch])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans