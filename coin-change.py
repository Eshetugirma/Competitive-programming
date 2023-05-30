class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        ans = float('inf')
        memo = {}
        def dp(curr):
            if curr == 0:
                return 0
            if curr in memo:
                return memo[curr]
            step = float('inf')
            for i in coins:
                if curr-i >= 0:
                    step = min(step,dp(curr-i))
            memo[curr] = step + 1
            return step+1
        ans = dp(amount)
        return ans if ans != float('inf') else -1