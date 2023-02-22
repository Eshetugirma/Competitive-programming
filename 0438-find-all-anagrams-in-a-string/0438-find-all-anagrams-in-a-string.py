class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        index = 0
        #===>>>>> diclare the dict
        window = Counter(s[:len(p)])
        target = Counter(p)  
        #==>>> check if there is anagram and append its starting index to ans
        for i in range(len(s)-len(p)):
            if window == target:
                ans.append(i)
            window[s[i]] -= 1
            window[s[i+len(p)]] += 1
            if window[s[i]] == 0:
                del window[s[i]]
            index = i+1
        #==>>> after loop ended check if there is anagram 
        if window == target:
            ans.append(index)
        return ans
                