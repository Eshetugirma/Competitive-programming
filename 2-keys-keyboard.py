class Solution:
    def minSteps(self, n: int) -> int:
        start = 2
        ans = 0
        while start*start <= n: 
            while not n%start :
                ans += start
                n //= start
            if start == 2:
                start += 1
            else:
                start += 2
        if n != 1:
            ans += n
        return ans