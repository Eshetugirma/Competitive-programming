class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if not char in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self 
        for i in range(len(word)):     
            char = word[i]  
            if char == ".": 
                for ch in node.children:

                    if node.children[ch].search(word[i+1:]): return True
                return False
            if char not in node.children: return False
            node = node.children[char]
        return node.isEnd

                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)