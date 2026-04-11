from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        idx = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, idx, l))
                idx += 1
        dummy = ListNode(0)
        current = dummy
        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
                idx += 1
        return dummy.next