class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        left = 0
        minimal = len(nums) + 1
        #===>>> for every sum in my window check if greater or equal to target
        for right in range(len(nums)):
            window += nums[right]
            #==>>then update minimum length of window and move the left
            while window >= target:
                minimal = min(minimal,right-left+1)
                window -= nums[left]
                left += 1
        if minimal > len(nums):
            return 0
        return minimal