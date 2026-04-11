from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hash_map = {}
        hash_map[head] = Node(head.val)
        current = head
        current_copy = hash_map[head]
        while current.next:
            current = current.next
            current_copy.next = Node(current.val)
            current_copy = current_copy.next
            hash_map[current] = current_copy
        current = head
        current_copy = hash_map[current]
        while current:
            if current.random:
                current_copy.random = hash_map[current.random]
            current = current.next
            if current:
                current_copy = hash_map[current]
        return hash_map[head]