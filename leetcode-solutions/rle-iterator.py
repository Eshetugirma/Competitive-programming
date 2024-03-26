class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.que = deque(encoding)
        

    def next(self, n: int) -> int:
        while self.que and self.que[0] < n:
            n -= self.que[0]
            self.que.popleft()
            self.que.popleft()
        if self.que and self.que[0] >= n:
            self.que[0] -= n
            return self.que[1]
        return -1
            

        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)