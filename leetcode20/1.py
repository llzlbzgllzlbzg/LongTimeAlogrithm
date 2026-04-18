class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0