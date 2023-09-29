class TrieNode:

    def __init__(self):
        self.children = {}
        self.cost = 0

class MapSum:

    def __init__(self):
        self.trie = TrieNode()
        self.seen = {}

    def insert(self, key: str, val: int) -> None:
        new = val
        if key in self.seen:
            val -= self.seen[key]
        # seen[key] = val
        self.seen[key] = new
        node = self.trie
        # node.cost = val
        for char in key:
            
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            node.cost += val
            

    def sum(self, prefix: str) -> int:
        node = self.trie
        ans = 0
        for char in prefix: 
            # ans = node.cost
            # print(ans)
            if char not in node.children: return 0
            node = node.children[char]
        # print(list(node.children))
        return node.cost

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)