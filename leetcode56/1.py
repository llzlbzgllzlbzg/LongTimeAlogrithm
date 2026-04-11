from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        img = []
        for i in intervals:            
            if not img or img[-1][1] < i[0]:
                img.append(i)
            else:
                img[-1][1] = max(img[-1][1],i[1])
        return img