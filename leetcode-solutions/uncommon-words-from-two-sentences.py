class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        s = (s1 + ' ' + s2)

        ss = Counter(list(s.split(' ')))

        ans = []

        for word,count in ss.items():
            if count == 1:
                ans.append(word)


        return ans
        