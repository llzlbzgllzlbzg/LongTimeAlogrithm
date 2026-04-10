class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_length = -1, len(s) + 1
        s_count, t_count = [0] * (ord('z') - ord('A') + 1), [0] * (ord('z') - ord('A') + 1)
        for i in t:
            t_count[ord(i) - ord('A')] += 1
        left = 0
        for right in range(len(s)):
            s_count[ord(s[right]) - ord('A')] += 1
            while left <= right and all(s_count[i] >= t_count[i] for i in range(len(s_count))):
                if right - left + 1 < ans_length:
                    ans_left, ans_length = left, right - left + 1
                s_count[ord(s[left]) - ord('A')] -= 1
                left += 1
        return s[ans_left:ans_left + ans_length] if ans_length <= len(s) else ''