class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1



class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i in range(len(words)):
            
            for j in range(len(words[i])):
                node = self.root
                temp = words[i][j:] + "#" + words[i]
                # print(temp)
                for char in temp:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                    node.index = i
                
                
    def f(self, pref: str, suff: str) -> int:
        node = self.root
        target = suff + "#" + pref
        # print(target)
        for char in target:
            
            if char in node.children:
                node = node.children[char]
                # temp = node
            else:
                return -1
        return node.index
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)