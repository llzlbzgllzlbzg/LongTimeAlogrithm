# 可以采用快慢指针,判断两个指针是否能相遇，也可以翻转链表,判断是否回到头节点,再翻转可以复原链表
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        hash_set = set()
        current = head
        while current:
            if current in hash_set:
                return True
            hash_set.add(current)
            current = current.next
        return False