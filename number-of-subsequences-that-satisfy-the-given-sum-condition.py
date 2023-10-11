class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9+7
        left = 0
        right = len(nums)-1
        ans = 0 
        while left <= right:
            if nums[right]+nums[left] > target:
                right -= 1
            else:
                ans += pow(2,right-left)%mod
                
                left += 1
        return ans%mod