class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        #==>>> this is just the same as fabonacci number
        def climb(n):
            if n < 2:
                return 1
            if not memo[n]:
                memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
        return climb(n)