class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = defaultdict(int)
        mx = 0
        for word in words:
            bitw = 0
            for c in word:
                bitw |= (1 << ord(c)-97)
            dic[word] = bitw
        for word1 in words:
            for word2 in words:
                if not (dic[word1] & dic[word2]):
                    mx = max(mx,len(word1)*len(word2))
        return mx