class Solution:
    def getDigits(self, s: str, ptr: list) -> str:
        ret = ""
        while ptr[0] < len(s) and s[ptr[0]].isdigit():
            ret += s[ptr[0]]
            ptr[0] += 1
        return ret

    def getString(self, v: list) -> str:
        return "".join(v)

    def decodeString(self, s: str) -> str:
        stack = []
        ptr = [0]

        while ptr[0] < len(s):
            cur = s[ptr[0]]
            if cur.isdigit():
                digits = self.getDigits(s, ptr)
                stack.append(digits)
            elif cur.isalpha() or cur == '[':
                stack.append(s[ptr[0]])
                ptr[0] += 1
            else:
                ptr[0] += 1
                sub = []
                while stack[-1] != '[':
                    sub.append(stack.pop())
                sub.reverse()
                stack.pop()
                rep_time = int(stack.pop())
                o = self.getString(sub)
                t = o * rep_time
                stack.append(t)

        return self.getString(stack)