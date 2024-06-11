class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window, left, zeros = 0, 0, 0
        for i in range(len(nums)):
            
            zeros += 1 - nums[i]
            while zeros > k and left <= i:
                zeros -= 1 - nums[left]
                left += 1
            window = max(window,i-left+1)
        return window