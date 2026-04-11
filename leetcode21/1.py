from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        current1 = list1
        current2 = list2
        result = ListNode()
        current = result

        while current1 is not None and current2 is not None:
            if current1.val < current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        if current1 is not None:
            current.next = current1
        if current2 is not None:
            current.next = current2

        return result.next