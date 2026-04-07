from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        for i in p:
            p_count[ord(i) - ord('a')] += 1
        s_count = [0] * 26
        result = []
        if len(s) < len(p):
            return result
        # 可以使用diff来统计不同的字符数量，减少比较的时间复杂度
        for i in range(len(p) - 1):
            s_count[ord(s[i]) - ord('a')] += 1
        left, right = 0, len(p) - 1
        while right < len(s):
            s_count[ord(s[right]) - ord('a')] += 1
            if s_count == p_count:
                result.append(left)
            s_count[ord(s[left]) - ord('a')] -= 1
            left += 1
            right += 1
        return result