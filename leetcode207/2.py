# 拓扑排序
from typing import List
from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        indeg = [0] * numCourses
        for pair in prerequisites:
            edges[pair[1]].append(pair[0])
            indeg[pair[0]] += 1
        queue = deque()
        count = 0
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
        while queue:
            count += 1
            cur = queue.popleft()
            for next in edges[cur]:
                indeg[next] -= 1
                if indeg[next] == 0:
                    queue.append(next)
        return count == numCourses