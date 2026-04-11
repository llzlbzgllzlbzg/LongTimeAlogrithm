from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            prev = end.next
            current = start
            while prev != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return end, start
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            start, end = reverse(group_prev.next, kth)
            group_prev.next = start
            end.next = group_next
            group_prev = end