class MedianFinder:

    def __init__(self):
        self.heap = []
        
    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        n = len(self.heap)
        self.heap.sort()
        if n%2:
            return self.heap[n//2]
        else:
            return (self.heap[n//2 -1]+self.heap[n//2])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()