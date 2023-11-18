class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        window = 0
        left = 0
        ans = 0
        for i in range(len(nums)):
            window += nums[i]
            while left <= i and ((window + k) // (i-left+1)) < nums[i]:
                window -= nums[left]
                left += 1
            ans = max(ans,i-left+1)
        return ans