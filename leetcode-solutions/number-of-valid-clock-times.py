class Solution:
    def countTime(self, time: str) -> int: 
        h1,h2,_,m1,m2 = time 
        ans = 1
        if h1 == '?' and h2 == '?':
            ans *= 24 
        elif h1 == '?':
            if int(h2) >= 4:
                ans *= 2
            else:
                ans *= 3
        elif h2 == '?':
            if int(h1) <= 1:
                ans *= 10
            else:
                ans *= 4
        
        if m1 == '?' and m2 == '?':
            ans *= 60
        elif m1 == '?':
            ans *= 6
        elif m2 == '?':
            ans *= 10
        return ans
