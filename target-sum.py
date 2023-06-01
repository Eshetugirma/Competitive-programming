class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in memo:
                return memo[(i,total)]
            memo[(i,total)] = dp(i+1,total+nums[i]) + dp(i+1,total-nums[i])
            return memo[(i,total)]
        return dp(0,0)