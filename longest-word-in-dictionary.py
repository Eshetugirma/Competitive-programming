class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        # self.val = ""
        # self.len = 0
        # self.ord = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,words):
        
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEnd = True
            # node.val = word
            # node.len = len(word)
            # node.ord = ord(word[-1])
        return self.root
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        root = trie.insert(words)
        dicts = defaultdict(list)
        for word in words:
            node = root
            flag = True
            for char in word:
                # temp = node
                node = node.children[char]
                if not node.isEnd:
                    flag = False
                    break
            if flag:
                dicts[len(word)].append(word)
        if not dicts: return ""
        return min(dicts[max(dicts.keys())])