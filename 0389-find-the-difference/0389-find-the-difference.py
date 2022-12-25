class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dics = {}
    
        for i in range(len(s)):
            dics[s[i]] = 1 + dics.get(s[i],0)

        newdics = {}
        for i in range(len(t)):
            newdics[t[i]] = 1 + newdics.get(t[i], 0)
            
        for char in t:
            if char not in dics or newdics[char] != dics[char]:
                return char