from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head
        def check(current):
            if current:
                if not check(current.next):
                    return False
                if current.val != self.front.val:
                    return False
                self.front = self.front.next
            return True
        return check(head)