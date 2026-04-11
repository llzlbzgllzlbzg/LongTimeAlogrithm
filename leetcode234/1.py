# 可以采用快慢指针+递归的方式判断链表是否为回文, 快慢指针找到链表中点, 快指针走一次两步, 慢指针走一次一步，然后通过翻转链表来判断链表是否为回文
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