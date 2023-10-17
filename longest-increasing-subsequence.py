class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n =len(nums)
        dp = [1]*n
        for i in range(n):
            curr = 0
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    curr = max(curr,dp[j])
            dp[i] = curr+1
        return max(dp)