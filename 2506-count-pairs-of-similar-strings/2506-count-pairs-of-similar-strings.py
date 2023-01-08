class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i,word in enumerate(words):
            for word2 in words[i+1:]:
                if set(word)==set(word2):
                    count += 1
        return count
    
    
   