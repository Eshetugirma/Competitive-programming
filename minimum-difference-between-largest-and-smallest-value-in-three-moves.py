class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        ans = float('inf')
        if len(nums) <= 4: return 0
        for i in range(4):
            ans = min(ans,nums[len(nums)-4+i] - nums[i])
        return ans