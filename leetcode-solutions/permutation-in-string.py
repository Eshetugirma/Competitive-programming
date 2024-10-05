class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        n = len(s1)
        m = len(s2)
        check = Counter(s2)
        for i in range(n-m+1):
            curr = Counter(s1[i:m+i])
            if curr == check:
                return True
        return False
