class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = 0
        left = 0
        for i in range(len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            ans = max(ans,curr)

        return ans


