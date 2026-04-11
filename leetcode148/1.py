from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_nodes = []
        current = head
        while current:
            list_nodes.append(current)
            current = current.next
        list_nodes.sort(key=lambda node: node.val)
        dummy = ListNode(0)
        current = dummy
        for node in list_nodes:
            current.next = node
            current = current.next
        current.next = None
        return dummy.next