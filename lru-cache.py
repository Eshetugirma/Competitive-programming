class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dic = defaultdict()
        self.que = deque()
    def get(self, key: int) -> int:
        
        if key in self.dic: 
            self.que.remove(key)
            self.que.append(key)
            return self.dic[key]
        else: return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            self.que.append(key)
        else:
            self.que.remove(key)
            self.que.append(key)
        self.dic[key] = value
        # print(self.que,self.dic)
        if self.capacity < len(self.que):
            LRU = self.que.popleft()
            # print(LRU)
            del self.dic[LRU]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)