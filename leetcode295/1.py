import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.odd = False
        

    def addNum(self, num: int) -> None:
        if self.odd:
            if num < -self.left[0]:
                heapq.heappush(self.left, -num)
                num = -heapq.heappop(self.left)
            heapq.heappush(self.right, num)
        else:
            if self.right and num > self.right[0]:
                heapq.heappush(self.right, num)
                num = heapq.heappop(self.right)
            heapq.heappush(self.left, -num)
            
        self.odd = not self.odd

    def findMedian(self) -> float:
        if self.odd:
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2