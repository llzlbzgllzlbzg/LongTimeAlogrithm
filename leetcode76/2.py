class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_length = -1, len(s) + 1
        s_count = {}
        t_count = {}
        for i in t:
            t_count[i] = t_count.get(i, 0) + 1
        left = 0
        valid = 0
        for right in range(len(s)):
            current = s[right]
            s_count[current] = s_count.get(current, 0) + 1
            if current in t_count and s_count[current] == t_count[current]:
                valid += 1
            while left <= right and valid == len(t_count):
                if right - left + 1 < ans_length:
                    ans_left, ans_length = left, right - left + 1
                s_count[s[left]] -= 1
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    valid -= 1
                left += 1
        return s[ans_left:ans_left + ans_length] if ans_length <= len(s) else ''