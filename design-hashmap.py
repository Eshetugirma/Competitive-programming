class MyHashMap:

    def __init__(self):
        self.my_hash = {}
        

    def put(self, key: int, value: int) -> None:
        self.my_hash[key] = value

    def get(self, key: int) -> int:
        if key in self.my_hash: return self.my_hash[key]
        else: return -1

    def remove(self, key: int) -> None:
        if key in self.my_hash :
            del self.my_hash[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)