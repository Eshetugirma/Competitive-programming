class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [inf]*n
        memo[0] = 0
        for i in range(n):
            for j in range(i+1,nums[i]+i+1):
                j = j%n
                memo[j] = min(memo[j],1+memo[i])
        return memo[-1]
        