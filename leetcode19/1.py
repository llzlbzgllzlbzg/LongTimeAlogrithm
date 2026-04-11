from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(0, head)
        current = dummy
        while current:
            stack.append(current)
            current = current.next
        for _ in range(n):
            stack.pop()
        stack[-1].next = stack[-1].next.next
        return dummy.next