class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hashMap = {}
        self.stack = deque()

    def get(self, key: int) -> int:
        if key in self.hashMap: 
            self.stack.remove(key)
            self.stack.append(key)
            return self.hashMap[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap :
            self.stack.remove(key)
            self.stack.append(key)
            self.hashMap[key] = value
        elif len(self.stack) < self.size:
            self.stack.append(key)
            self.hashMap[key] = value

        else:
            del self.hashMap[self.stack[0]]
            self.stack.popleft()
            self.stack.append(key)
            self.hashMap[key] = value




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)