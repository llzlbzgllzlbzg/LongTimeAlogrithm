# 可以采用递归的方式翻转链表, 递归表达式为current.next.next = current, current.next = None
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev