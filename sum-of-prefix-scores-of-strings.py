class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def Insert(self,words):
        # node = self.root
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1
                
        return self.root
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        root = trie.Insert(words)
        # print(node.children)
        ans = []
        for word in words:
            count = 0
            node = root
            for char in word:
                # print(node.children)
                node = node.children[char]
                count += node.count
            ans.append(count)

        return ans