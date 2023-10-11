class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:      
        target,window = 0,0
        t = len(s1)
        n = len(s2)
        if t > n: return False
        # print(ord("a"))
        for i in range(t):
            target += 26**((ord(s1[i])-96))
            window += 26**((ord(s2[i])-96))
            target = target%(10**9+7)
            window = window%(10**9+7)
        if window == target: return True
        for right in range(t,n):
            window -= 26**(ord(s2[right-t])-96)
            window += 26**(ord(s2[(right)])-96)
            window = window%(10**9+7)
            # print(target,window)
            
            if target == window: return True
        return False