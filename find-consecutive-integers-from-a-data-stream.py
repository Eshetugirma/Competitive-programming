class DataStream:

    def __init__(self, value: int, k: int):
        #==>> define value and k as global variable
        self.queue = deque()
        self.k = k
        self.value = value
        self.count = 0

    def consec(self, num: int) -> bool:
        #==>>> append every num to queue until len of queue is equal to k if so popleft
        self.queue.append(num)
        if num != self.value:
            self.count += 1
        if len(self.queue) > self.k:
            if self.queue.popleft() != self.value:
                self.count -= 1
            
        return len(self.queue) == self.k and not self.count
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)