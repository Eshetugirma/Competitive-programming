class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.list = [""]*n
        self.start = 1
        self.seen = set()
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey-1] = value
        
        if idKey > self.start:
            
            return []
        else:
            i = idKey-1
            while i < self.n and self.list[i]:
                i += 1
            self.start = i+1
            return self.list[idKey-1:i]


        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)