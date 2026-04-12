from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        for i in range(numCourses):
            queue.append(i)
        count = 0
        while queue:
            length = len(queue)
            hashmap = set()
            for _ in range(length):
                head = queue.popleft()
                hashmap.add(head)
            for pair in prerequisites:
                if pair[0] in hashmap:
                    queue.append(pair[1])
            if count > numCourses:
                return False
            count += 1
        return True