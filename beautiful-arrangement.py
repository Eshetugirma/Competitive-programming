class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        def backtrack(visited):
            nonlocal ans
            if visited.bit_count() == n:
                ans += 1
                return 
            for i in range(1,n+1):
                #==>>> check if visited
                if visited & (1 << i):
                    continue
                #===>>>> check divisiblity which considered as beautiful arrangement
                if not visited  or (not i % (visited.bit_count()+1) or not (visited.bit_count()+1)%i):
                    visited |= 1 << (i)
                    backtrack(visited)
                    visited &= ~(1 << i)
        backtrack(0)
        return ans